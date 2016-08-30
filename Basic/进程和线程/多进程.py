import os
import random

from multiprocessing import Process

import time


# def run_proc(name):
#     print("Run child proceess %s (%s)..." % (name, os.getpid()))
#
#
# if __name__ == "__main__":
#     print("Parent process %s." % os.getpid())
#     p = Process(target=run_proc, args=("test",))
#     print("Child process will start.")
#     p.start()
#     p.join()
#     print("Child process end.")


# ThreadPool
from multiprocessing.pool import Pool

import subprocess


def long_time_task(name):
    print("Run task %s (%s)" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time .time()
    print("Task %s runs %0.2f seconds" % (name, (end - start)))


if __name__ == "__main__":
    print('Parent process %s.' % os.getpid())
    p = Pool(5)
    for i in range(6):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


#
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

