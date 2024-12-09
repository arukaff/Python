from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator,BranchPythonOperator
import pandas as pd
from sqlalchemy import create_engine
import os

def save_in_db(ti):
    df = ti.xcom_pull(task_ids='transform_data')
    db_url = "mysql+mysqlconnector://root:Nagual45@localhost:3306/sakila"
    engine = create_engine(db_url, echo=False)

    with engine.begin() as conn:
        
        df.to_sql(
            name='air', # database table
            if_exists='append',
            con=conn, # database connection
            index=False # Don't save index
        )
    print('Данные сохранены:',df.head())

def load_data(data):
    print(os.getcwd())
    #data=data+'.csv'
    df=pd.read_csv(data,header=0, engine='python')
    print(df)
    return df
def transform_data(ti):
   
    print('Начинаем обработку')
    dfs = ti.xcom_pull(task_ids=[
    'load_file_booking.csv',
    'load_file_client.csv',
    'load_file_hotel.csv'
    ])
    print('Полученные данные',dfs[0], dfs[1],dfs[2])
    res = pd.merge(dfs[0], dfs[1], on='client_id')
    res = pd.merge(res, dfs[2], on='hotel_id')
    res['booking_date'] = res['booking_date'].str.replace('/','-')
    res.dropna(subset=['currency'], inplace=True)
    res = res.drop_duplicates()
    res.loc[res['currency'] == 'EUR', 'booking_cost'] = res['booking_cost'].astype('float')*1.3
    res.loc[res['currency'] == 'EUR', 'currency'] = 'GBP'
    print(res)
    return res

with DAG("get_trans_data", start_date=datetime(2021, 1 ,1), schedule_interval='@daily', catchup=False) as dag:        
    load_data_tasks = [
        PythonOperator(
        task_id=f"load_file_{file_name}",
        python_callable=load_data,
        op_kwargs={"data": file_name}
        ) for file_name in ['booking.csv','client.csv','hotel.csv']
    ]
    transform_data_task = PythonOperator(
        task_id='transform_data', 
        python_callable=transform_data
        )
    save_in_db_task = PythonOperator(
        task_id="save_in_db",
        python_callable=save_in_db
        )
    

load_data_tasks >> transform_data_task >> save_in_db_task
