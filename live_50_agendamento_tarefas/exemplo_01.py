""" Exemplo de uma tarefa que diz a hora."""

import sched
import time
scheduler = sched.scheduler()

def diga_tempo():
    print(time.ctime())
    scheduler.enter(delay=10, priority=0, action=diga_tempo)

diga_tempo()

try:
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print('Parei com sched')

