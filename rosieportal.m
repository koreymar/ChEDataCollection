%% Test

clear;

startdate = '2022-03-16';
enddate = '2022-03-16';
starttime = '14:00';
endtime = '16:50';
interval = '30s';
area = '150';

endpoint = 'http://192.168.100.58:5000/csv?';
dates_times = append('startdate=', startdate, '&enddate=', enddate, '&starttime=', starttime, '&endtime=', endtime);
url = append(endpoint, dates_times, '&interval=', interval, '&area=', area);

options = weboptions;
options.Timeout = 25;

labdata1 = webread(url, options);
disp('Done');
