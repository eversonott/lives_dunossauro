""" Exemplo de uma tarefa que diz a hora."""

import sched
import time
scheduler = sched.scheduler()


def diga_tempo():
    print(time.ctime())
    scheduler.enter(delay=10, priority=1, action=diga_tempo)

def ola():
    print('Olá')
    scheduler.enter(delay=5, priority=0, action=ola)

def start():
    scheduler.enter(delay=10, priority=1, action=diga_tempo)
    scheduler.enter(delay=5, priority=0, action=ola)

start()

try:
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print('Parei com sched')

