"""
Basic Python script to download data from the UO Lab System. Must be on campus or using the RHIT VPN
David Henthorn, RHIT 2022
"""

# Requires the pandas dataframe library. May need to install it
import pandas as pd

# Change these. Be sure to use YYYY-MM-DD date format and 24 hour clocks (2:00PM is 14:00). All times RHIT local.
startdate = '2022-03-16'
enddate = '2022-03-16'
starttime = '14:00'
endtime = '16:50'
area = '150'    # 150 is Reverse Osmosis, 300 is Fluid Flow, etc.
interval = '30s' # 30s is most common, but other values may be chosen

data_URL = 'http://uolab.rose-hulman.edu:5080/csv?starttime=' + starttime + '&endtime=' + endtime + '&startdate=' + startdate
data_URL += '&enddate=' + enddate + '&area=' + area + '&interval=' + interval

df = pd.read_csv(data_URL)

print(df.info())

df.head()