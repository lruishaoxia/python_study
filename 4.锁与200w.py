import threading
from threading import *
import time

g_num = 0


def work1(a):
    global g_num
    for i in range(a):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print('w1:{}'.format(g_num))


def work2(a):
    global g_num
    for i in range(a):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print('w2:{}'.format(g_num))


if __name__ == '__main__':
    mutex = threading.Lock()
    w1 = Thread(target=work1,args=(1000000,))
    w2 = Thread(target=work2,args=(1000000,))
    w1.start()
    w2.start()
    w1.join()
    w2.join()
    print('final result:%d'%g_num)

