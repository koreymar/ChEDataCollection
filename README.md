# ChE Data Collection Website
Flask app created by Eddie Barry (RHIT CHE class of 2022) and David Henthorn (RHIT CHE).

Runs two ways:

The / endpoint is a simple interactive website for data download.

The /csv endpoint uses a query string and is amenable to Python, Matlab, etc. 
Example usage is: http://hostname:port/csv?startdate=2022-05-01&starttime=18:00&enddate=2022-05-02&endtime=4:00&interval=10s&area=150

When running, allows users to query a website to select which data to download from a OSIsoft PI data archive.

Server must be running the PI SDK, which means this works only on Windows machines. Clients connect from any web browser that can accept a CSV file download.

