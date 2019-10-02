"""Add radio show to cronjob

Usage:
  schedule <url> <title> <cron> <hours>

Arguments:
  <url>     Streaming audio source
  <title>   Show title, output files will be uniquely named according to start
            time.
  <cron>    Cron specifier, e.g. "0 14 * * *"
  <hours>   Duration, in hours.
"""
import docopt

from radioat.radio_program import RadioProgram
from radioat.radio_station import RadioStation
from radioat.schedule_source import Schedule
from radioat.times import Times


def main():
    args = docopt.docopt(__doc__)
    url = args["<url>"]
    title = args["<title>"]
    cron = args["<cron>"]
    duration = float(args["<hours>"])

    Schedule.add_recurring(
        RadioProgram(
            station=RadioStation(url),
            title=title,
            times=Times(cron, duration)))


if __name__ == "__main__":
    main()
