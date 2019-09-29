import datetime
import sys

import radioat.radio_program
import radioat.radio_station
import radioat.schedule_source
import radioat.times


def main():
    # TODO: usage
    url = sys.argv[1]
    title = sys.argv[2]
    cron = sys.argv[3]
    # FIXME: double-converting is crazy
    #hours = float(sys.argv[4])
    #seconds = 3600 * hours
    #duration = datetime.timedelta(seconds=seconds)
    duration = float(sys.argv[4])

    station = radioat.radio_station.RadioStation(url)
    times = radioat.times.Times(cron, duration)
    program = radioat.radio_program.RadioProgram(station=station, title=title, times=times)
    radioat.schedule_source.Schedule.add_recurring(program)


if __name__ == "__main__":
    main()
