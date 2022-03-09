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
    print(g_num)