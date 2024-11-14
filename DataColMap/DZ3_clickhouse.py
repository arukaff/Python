from clickhouse_driver import Client
import json

with open('DataColMap/crash-data.json', 'r') as f:
    data=json.load(f)

db_data=[]
for i in range(10):
    db_data.append([data['features'][i]['properties']["tamainid"],data['features'][i]['properties']["location_description"],data['features'][i]['properties']["lon2"],data['features'][i]['properties']["lat2"]])
print(db_data) 


client = Client(host='localhost',  # Use 'localhost' or '127.0.0.1' for a local server
                user='default',    # Default user, adjust if you've changed the user
                password='',       # Default installation has no password for 'default' user
                port=9000)         # Default TCP port for ClickHouse


try:
    
    client.execute('CREATE DATABASE IF NOT EXIST my_bd')
    client.execute('''CREATE TABLE IF NOT EXIST new_table (tamainid UInt32, location_description String, lon2 Float64, lat2 Float64) ENGINE MergeTree ORDER BY tamainid''')
    client.execute('INSERT INTO new_tabe (tamainid, location_description String, lon2, lat2 VALUES', db_data)
    result = client.execute('SHOW TABLES')
    print(result)
    result = client.execute('SELECT * FROM new_table')
    print(result)
 

except Exception as e:
    print(f"Encountered an error: {e}")


