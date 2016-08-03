'''
'''

import datetime
import requests

import ui

class RadioSource(object):
    '''
    Connect to an URL and supply raw data in streaming chunks.
    '''
    def __init__(self, station):
        self.station = station

    def record(self, duration):
        start_time = datetime.datetime.utcnow()
        end_time = start_time + duration
        ui.get().log("Recording from {now} until {end_time}".format(now=start_time, end_time=end_time))

        response = requests.get(self.station.url, stream=True, timeout=10).raw

        # TODO: reconnect and resume if necessary.  write about it in a log and metadata
        # TODO: use automatic chunk size rather than the default?
        #for chunk in response.iter_content(chunk_size=None):
        for chunk in response:
            if datetime.datetime.utcnow() > end_time:
                return
            yield chunk
