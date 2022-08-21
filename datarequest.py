"""
DataRequest class
David Henthorn, Rose-Hulman Chemical Engineering, 2022
"""

from datetime import datetime, timedelta
from labarea import LabArea


class DataRequest:

    def __init__(self, args):

        self.datetime_format = '%Y-%m-%d %H:%M'
        self.max_delta = timedelta(hours=24)
        self.args = args
        self.startdate = self.args.get('startdate')
        self.enddate = self.args.get('enddate')
        self.starttime = self.args.get('starttime')
        self.endtime = self.args.get('endtime')
        self.interval = self.args.get('interval')
        self.area = self.args.get('area')
        self.labarea = LabArea(self.area)
        self.request_errors = []
        self.is_valid = False

        # Create timestamps for the start and end and while doing so check if they are valid
        if self.startdate and self.starttime:
            # Make a datetime string of format self.datetime_format
            start = self.startdate + " " + self.starttime

            # Try to create the datetime objects and catch the exception if they fail
            try:
                self.date1 = datetime.strptime(start, self.datetime_format)
            except ValueError:
                self.date1 = None
                self.request_errors.append('Start date ' + self.startdate + ' is not in form YYYY-MM-DD ' +
                                           'or start time ' + self.starttime + ' is invalid')

        if self.enddate and self.endtime:
            end = self.enddate + " " + self.endtime
            try:
                self.date2 = datetime.strptime(end, self.datetime_format)
            except ValueError:
                self.date2 = None
                self.request_errors.append('End date ' + self.enddate + ' is not in form YYYY-MM-DD ' +
                                       'or end time ' + self.endtime + ' is invalid')

    def __repr__(self):
        rep = 'Request is for area ' + self.area + ' every ' + self.interval + ' seconds from '
        rep += self.startdate + ' ' + self.starttime + ' to '
        rep += self.enddate + ' ' + self.endtime
        return rep

    def errors_to_html(self):
        """
        Returns the list of errors as a simple html page
        """

        response = '<html><body>'
        response += 'The request contained the following error(s):<br><br><br>'
        for err in self.request_errors:
            response += ('' + err + '<br>')
        response += ('<br><br>Example usage: http://hostname:port/csv?startdate=2022-05-01&starttime=18:00'
                        + '&enddate=2022-05-02&endtime=4:00&interval=10s&area=150 <br>')
        response += '</body></html>'
        return response

    def errors_to_text(self):
        """
        Returns the list of errors as a simple html page
        """

        response = 'The request contained the following error(s):'
        for err in self.request_errors:
            response += (' ' + err + '.')
        return response

    def check_datetime(self):
        """
        Method checks the following:
        1. Are the start and end date/times in the correct form?
        2. Are the start and end date/times within a max window (say 1 day)
        No values are returned, but errors are added to the .request_errors list

        # Time/dates are valid. Let's check to see if they follow rules of
        #   * Start must be before end
        #   * (End - Start) must be less than a set value (say 1 day)
        """

        delta = self.date2 - self.date1

        if delta.days < 0:
            self.request_errors.append('Starting date and time must be before ending date and time')

        if delta > self.max_delta:
            self.request_errors.append('Elapsed time between start and end exceeds max value of '
                                       + str(self.max_delta) + ' seconds')
        return

    def validate(self):
        """ This method looks at the incoming request make sure all parts are completed
        and that those values (start times, etc.) make sense
        No return value. Sets the value of .is_valid to True/False
        """

        if self.startdate is None:
            self.request_errors.append('No startdate in URL query string')

        if self.enddate is None:
            self.request_errors.append('No enddate in URL query string')

        if self.starttime is None:
            self.request_errors.append('No starttime in URL query string')

        if self.endtime is None:
            self.request_errors.append('No endtime in URL query string')

        # Check to see if an area is provided. Then check whether it's on the allowed list
        if self.area is None:
            self.request_errors.append('No area in URL query string')
        elif not self.labarea.allowed:
            self.request_errors.append('Area ' + self.area + ' does not exist')

        if self.interval is None:
            self.request_errors.append('No interval in URL query string')

        # Now check the dates and times
        if len(self.request_errors) == 0:
            self.check_datetime()

        # If we still have no errors, denote the request as valid
        if len(self.request_errors) == 0:
            self.is_valid = True
        return
