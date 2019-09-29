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

import radioat.radio_program
import radioat.radio_station
import radioat.schedule_source
import radioat.times


def main():
    args = docopt.docopt(__doc__)
    url = args["<url>"]
    title = args["<title>"]
    cron = args["<cron>"]
    duration = float(args["<hours>"])

    station = radioat.radio_station.RadioStation(url)
    times = radioat.times.Times(cron, duration)
    program = radioat.radio_program.RadioProgram(
        station=station, title=title, times=times)
    radioat.schedule_source.Schedule.add_recurring(program)


if __name__ == "__main__":
    main()
