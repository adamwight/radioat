# TODO:
# sudo -n true
# multiple providers

import crontab

class Schedule(object):
    #def add(station, times):

    def add_recurring(program):
        cron = crontab.CronTab(user=True)
        cmd = """
            {root}/bin/record_now "{url}" "{title}"
        """.format(root=__path__, url=program.station.url, title=program.title)
        job = cron.new(command=cmd)
        job.setall(program.times.crontab())
        cron.write()

    #def add_exception(program, times):
