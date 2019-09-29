# TODO:
# sudo -n true
# multiple providers

import crontab
import os

crontab_tpl = """
PYTHONPATH={root} {root}/bin/record_now "{url}" "{title}" {duration}
"""


class Schedule(object):
    # def add(station, times):

    # FIXME: __path__
    root = os.getenv("HOME") + "/radioat"

    @staticmethod
    def add_recurring(program):
        cron = crontab.CronTab(user=True)
        # TODO: upsert the entry, don't duplicate
        cmd = crontab_tpl.format(
            root=Schedule.root,
            url=program.station.url,
            title=program.title,
            duration=program.times.duration)
        job = cron.new(command=cmd)
        job.setall(program.times.crontab)
        print("Writing new crontab:\n" + cron.render()
              + "# " + job.description())
        cron.write()

    # def add_exception(program, times):
