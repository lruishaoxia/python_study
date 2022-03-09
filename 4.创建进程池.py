
from multiprocessing import Manager,Pool
import os,time

def writer(q):
    print('writer starts')
    for i in range(5):
        q.put(i)

def reader(q):
    print('reader starts')
    # while True:
    #     if  not q.empty():
    #         print('get {} from q'.format(q.get()))
    #     else:
    #         break
    for i in range(q.qsize()):
        print('get {} from q'.format(q.get()))
if __name__ == '__main__':
    q = Manager().Queue()
    po = Pool()
    po.apply_async(writer,args=(q,))
    time.sleep(1)
    po.apply_async(reader,args=(q,))
    po.close()
    po.join()
