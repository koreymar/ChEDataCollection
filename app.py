"""
PI Connect Flask App
Flask app which utilizes the PI SDK on Windows to connect to a PI server
and select datapoints for download as a CSV file
2022, Eddie Barry and David Henthorn
"""
CONST_NAME = "PI Connect Flask App"
CONST_VER = "0.02"
CONST_AUTHORS ="Eddie Barry (RHIT ChE, class of 2022) and David Henthorn, RHIT Professor"

# Requires the PIconnect package be installed. This package will install under various OS's, but
# it only functions on Windows machines with the PI SDK installed and properly setup
import PIconnect as PI

from flask import Flask, render_template, request, make_response
import pandas as pd
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', datefmt='%Y/%m/%d %H:%M:%S', level=logging.INFO)

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    logging.info("New request for /home from %s", request.remote_addr)
    return render_template('home.html')


@app.route('/download', methods=["POST"])
def download():
    project = request.form.get("project")
    logging.info("Received download request for project %s from IP %s", project, request.remote_addr)
    date = request.form.get("start")
    start_time = request.form.get("starttime")
    end_time = request.form.get("endtime")
    interval = request.form.get("interval")

    project_num = "*" + project + "*"
    project_start = date + " " + start_time
    project_end = date + " " + end_time

    logging.info("Requested dataset with start time of %s, end time of %s, and interval of %s", project_start, project_end, interval)

    if project_num == "*300*":
        search_term = "*-3*"
    else:
        search_term = project_num

    points = server.search(search_term)

    if len(points) == 0:
        logging.error("Found no PI datapoints for search term %s", search_term)
        response = None
    else:
        logging.info("Found %s PI points for project %s", len(points), project)
        df = pd.concat([point.interpolated_values(project_start, project_end, interval).to_frame(point.name + ' '
            + point.units_of_measurement) for point in points], axis = 1)

        df.index.rename('Timestamp', inplace = True)

        response=make_response(df.to_csv())
        cd = 'attachment; filename=CHE Lab Data.csv'
        response.headers['Content-Disposition'] = cd
        response.mimetype = 'text/csv'
        logging.info("Sending CSV file over http with response info %s", response)
        return response


if __name__ == '__main__':
    logging.info("Starting %s version %s", CONST_NAME, CONST_VER)
    logging.info("Written by %s", CONST_AUTHORS)

    # Let's attempt to keep the PI server connection open here in main. Otherwise, we need to connect each time
    # we enter the /download route, which results in much longer wait times

    logging.info("Attempting to connect to PI Server using the PI SDK")
    PI.PIConfig.DEFAULT_TIMEZONE = 'America/Indianapolis'
    with PI.PIServer() as server:
        logging.info("Connected to PI Server %s which is running version %s", server.server_name, server.version)
        app.run()


