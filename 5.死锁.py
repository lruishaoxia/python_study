import threading
import time

def work1():
    mutex1.acquire()
    print('w1 start')
    time.sleep(1)
    mutex2.acquire()
    print('w1 need m2')
    mutex2.release()
    mutex1.release()


def work2():
    mutex2.acquire()
    print('w2 start')
    time.sleep(1)
    mutex1.acquire()
    print('w2 need m1')
    mutex1.release()
    mutex2.release()
if __name__ == '__main__':
    mutex1 = threading.Lock()
    mutex2 = threading.Lock()
    w1 = threading.Thread(target=work1)
    w2 = threading.Thread(target=work2)
    w1.start()
    w2.start()
    w1.join()
    w2.join()

