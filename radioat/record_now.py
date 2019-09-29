"""
Record immediately.

Usage:
  record_now <url> <title> <hours>

Arguments:
  <url>     Streaming audio source
  <title>   Show title, output files will be uniquely named according to start
            time.
  <hours>   Floating point show length, for example "1.5" (90 minutes).

Options:
  -h --help     Show this screen.

"""
import datetime
import docopt
import sys
import threading

import radioat.archive_file
import radioat.radio_program
import radioat.radio_source
import radioat.radio_station
import radioat.ui


class RecordJob(object):

    def __init__(self, program, duration):
        self.start_time = datetime.datetime.utcnow()
        self.end_time = self.start_time + duration
        self.duration = duration
        self.bytes_written = 0

        reader = radioat.radio_source.RadioSource(program.station).record(duration)
        new_archive = radioat.archive_file.ArchiveFile(program)

        if sys.stdout.isatty():
            self.watchdog()

        with new_archive.sink as writer:
            for chunk in reader:
                writer.write(chunk)

                self.bytes_written += len(chunk)

        radioat.ui.get().log("Completed successfully, wrote {bytes}".format(bytes=radioat.ui.sizeof_fmt(self.bytes_written)))

    def watchdog(self):
        radioat.ui.get().progress(self)

        # FIXME: thread-dangerous
        thread = threading.Timer(1.0, self.watchdog)
        thread.daemon = True
        thread.start()


def doMain(url, title, hours, stdscr=None):
    # wired wrong
    if stdscr:
        radioat.console.stdscr = stdscr

    args = docopt.docopt(__doc__)
    seconds = 3600 * hours
    duration = datetime.timedelta(seconds=seconds)

    station = radioat.radio_station.RadioStation(url)
    program = radioat.radio_program.RadioProgram(station=station, title=title)
    RecordJob(program, duration)


def main():
    args = docopt.docopt(__doc__)

    if sys.stdout.isatty():
        import radioat.console
        radioat.ui.set(radioat.console.Console())
    else:
        import radioat.daemon
        radioat.ui.set(radioat.daemon.Daemon())

    radioat.ui.get().main = \
        lambda stdscr: doMain(args["<url>"], args["<title>"], float(args["<hours>"]), stdscr)
    radioat.ui.get().run()


if __name__ == "__main__":
    main()
