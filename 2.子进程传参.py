<<<<<<< HEAD
from multiprocessing import Process
import time

g_num = [1, 2]


def run_proc(name,**kwargs):
    g_num.append(1)
    for i in range(10):
        print('{}子进程正在运行{}'.format(name,kwargs))
        time.sleep(0.2)

if __name__ == '__main__':
    p = Process(target=run_proc,args=('一号',),kwargs={'tel':123})
    p.start()
    time.sleep(3)
    print(g_num)
    p.join()
=======
from multiprocessing import Process
import time

g_num = [1, 2]


def run_proc(name,**kwargs):
    g_num.append(1)
    for i in range(10):
        print('{}子进程正在运行{}'.format(name,kwargs))
        time.sleep(0.2)

if __name__ == '__main__':
    p = Process(target=run_proc,args=('一号',),kwargs={'tel':123})
    p.start()
    time.sleep(3)
    print(g_num)
    p.join()
>>>>>>> e2c43e045d170dddd8b48902e123096581e081ef
    print(g_num)