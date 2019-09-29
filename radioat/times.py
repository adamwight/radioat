class Times(object):
    def __init__(self, crontab=None, duration=None):
        # TODO: accessors for different schedule sources
        self.crontab = crontab
        self.duration = duration
