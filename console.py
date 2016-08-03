'''
Console GUI
'''

import curses
import datetime
import sys

stdscr = None

log_pos = [12, 5]
progress_pos = [12, 20]

class Console(object):
    main = None

    def run(self):
        curses.wrapper(self.main)

    def progress(self, job):
        # TODO: maybe provide a force parameter for crash reporting?

        now = datetime.datetime.utcnow()
        # Floor for rounded display
        now = now.replace(microsecond=0)

        percent_complete = (now - job.start_time).total_seconds() / job.duration.total_seconds()
        remaining = job.end_time - now
        # Floor
        remaining -= datetime.timedelta(microseconds=remaining.microseconds)

        stdscr.addstr(
            progress_pos[1], progress_pos[0],
            "{now}, {bytes} bytes written ({complete:.1f}%, {remaining} remaining)".format(
                now=now.isoformat(' '),
                bytes=ui.sizeof_fmt(job.bytes_written),
                complete=percent_complete, remaining=remaining))
        stdscr.refresh()

    def log(self, txt):
        stdscr.addstr(log_pos[1], log_pos[0], txt)
        # FIXME: cycle or stack
        log_pos[1] += 1
        stdscr.refresh()

