"""Marcar um veneto em um tempo específico"""
import sched
import time

from datetime import datetime, timedelta

scheduler = sched.scheduler(timefunc=time.time)

def reschedule():
    """Zere os segundos de now e some mais 1 minuto """
    new_target = datetime.now().replace(second=0, microsecond=0)
    new_target += timedelta(seconds==10)
    print(new_target)

    scheduler.enterabs(new_target.timestamp(), priority=0, action=saytime)

def saytime():
    print(time.ctime())
    reschedule()

reschedule()

scheduler.run(blocking=True)
