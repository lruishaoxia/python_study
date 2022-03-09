import os
import time
from multiprocessing import Process

def run_poc():
    print('pid={}'.format(os.getpid()))
    while True:
        print('子进程在运行')
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=run_poc)
    p.start()
    print('pid={}'.format(os.getpid()))
    while True:
        print('父进程在运行')
        time.sleep(1)
