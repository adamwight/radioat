'''
'''

import datetime
import requests

class RadioSource(object):
    def __init__(self, station):
        self.station = station

    def record_to(self, output, duration):
        response = requests.get(self.station.url, stream=True, timeout=10).raw
        now = datetime.datetime.utcnow()
        end_time = now + duration
        print "Recording from {now} until {end_time}".format(now=now, end_time=end_time)
        # TODO: reconnect and resume if necessary.  write about it in a log and metadata
        # TODO: Should be a generator instead
        #for chunk in response.iter_content(chunk_size=None):
        for chunk in response:
            output.write(chunk)
            if datetime.datetime.utcnow() > end_time:
                return
