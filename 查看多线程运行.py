import threading


def sing():
    while True:
        pass


def dance():
    while True:
        pass

if __name__ == '__main__':
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()