# ChE Data Collection Website
Flask app created by Eddie Barry (RHIT CHE class of 2022) and David Henthorn (RHIT CHE).

Allows users to query a website and pull data from an OSIsoft PI data archive.

Also exposes a /csv route for direct downloads to clients.

Server must be running the PI SDK, which means this works only on Windows machines. Clients connect from any web browser that can accept a CSV file download.

Clients for Python, Python Notebooks (Jupyter), Julia, and Matlab are included.

