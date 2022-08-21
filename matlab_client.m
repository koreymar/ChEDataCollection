%% Simple Matlab client to download data
%% Need to make sure you are on the campus network or connected to the RHIT VPN

clear;
% Dates should be of form YYYY-MM-DD
startdate = '2022-03-16';
enddate = '2022-03-16';

% Use 24 hour clock times (e.g. 2:00PM is 14:00)
starttime = '14:00';
endtime = '16:50';

% Requesting data every 30 seconds ('30s') is most common, but can change this
interval = '30s';

% Change this to match your Lab area (e.g. Fluid Flow is area '300')
area = '150';


endpoint = 'http://uolab.rose-hulman.edu:5080/csv?';
dates_times = append('startdate=', startdate, '&enddate=', enddate, '&starttime=', starttime, '&endtime=', endtime);
url = append(endpoint, dates_times, '&interval=', interval, '&area=', area);

% Give the website up to 20 seconds to respond
options = weboptions;
options.Timeout = 20;

labdata = webread(url, options);
disp('Done. Requested data is in the labdata table');
