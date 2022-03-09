import time
from multiprocessing import Process, Queue
def writer(q:Queue):
    for i in ('A','B','C'):
        print('put {} to queue'.format(i))
        q.put(i)
        time.sleep(1)

def reader(q:Queue):
    while True:
        if not q.empty():
            i = q.get()
            print('get {} from queue'.format(i))
            time.sleep(1)
        else:
            break

if __name__ == '__main__':
    q = Queue(10)
    pw = Process(target=writer,args=(q,))
    pr = Process(target=reader,args=(q,))
    pw.start()
    time.sleep(3)
    pr.start()
    pw.join()
    pr.join()