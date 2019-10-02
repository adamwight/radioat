'''
'''

import datetime
import requests

import radioat.ui


class RadioSource(object):
    '''
    Connect to an URL and supply raw data in streaming chunks.
    '''
    def __init__(self, station):
        self.station = station

    def record(self, duration):
        start_time = datetime.datetime.utcnow()
        end_time = start_time + duration
        radioat.ui.get().log("Recording from {now} until {end_time}".format(
            now=start_time, end_time=end_time))

        # TODO: context manager, raise_for_status
        response = requests.get(self.station.url, stream=True, timeout=10).raw

        # TODO: reconnect and resume if necessary.  write about it in a log and
        # metadata TODO: use automatic chunk size rather than the default?
        #   for chunk in response.iter_content(chunk_size=None):
        for chunk in response:
            yield chunk
            if datetime.datetime.utcnow() > end_time:
                return
