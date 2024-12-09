#pip install SQLAlchemy
#pip install mysql-connector-python
import pandas as pd
from sqlalchemy import create_engine
import os


#df=pd.read_csv('pollution_subset.csv',header=0, engine='python')
def save_in_db(df):
    # db_url = "mysql+mysqlconnector://root:Nagual45@localhost:3306/sakila"
    # engine = create_engine(db_url, echo=False)

    # with engine.begin() as conn:
        
    #     df.to_sql(
    #         name='air', # database table
    #         if_exists='append',
    #         con=conn, # database connection
    #         index=False # Don't save index
    #     )
    print('Данные сохранены:',df.head())
def load_data(data):
    print(os.getcwd())
    data=data+'.csv'
    df=pd.read_csv(data,header=0, engine='python')
    return df
def transform_data():
    fn=['booking','client','hotel']
    dfs=[]
    for f in fn:
        dfs.append(load_data(f))
    res = pd.merge(dfs[0], dfs[1], on='client_id')
    res = pd.merge(res, dfs[2], on='hotel_id')
    res['booking_date'] = res['booking_date'].str.replace('/','-')
    res.dropna(subset=['currency'], inplace=True)
    res = res.drop_duplicates()
    res.loc[res['currency'] == 'EUR', 'booking_cost'] = res['booking_cost'].astype('float')*1.3
    res.loc[res['currency'] == 'EUR', 'currency'] = 'GBP'
    print(res)

transform_data()
