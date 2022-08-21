import pandas as pd
from flask import request

print('Running the client')

startdate = '2022-03-16'
enddate = '2022-03-16'
starttime = '14:00'
endtime = '16:50'
area = '150'
interval = '30s'

data_URL = 'http://127.0.0.1:5000/csv?starttime=' + starttime + '&endtime=' + endtime + '&startdate=' + startdate
data_URL += '&enddate=' + enddate + '&area=' + area + '&interval=' + interval

request
print(data_URL)

df = pd.read_csv(data_URL)
print(df.info)
df.head()