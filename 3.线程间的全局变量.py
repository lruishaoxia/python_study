from threading import Thread
import time

g_num = [1, 2, 3]


def work1():
    global g_num
    a.append(4)
    print(a)


def work2():
   global g_num
   print(a)

if __name__ == '__main__':
    w1 = Thread(target=work1)
    w2 = Thread(target=work2)
    w1.start()
    time.sleep(1)
    w2.start()