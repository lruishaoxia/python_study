import socket
import select
import sys

def tcp_client():
    if len(sys.argv) == 1:
        return
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_addr = (sys.argv[1], 2000)
    c.connect(dest_addr)
    epoll = select.epoll()
    epoll.register(c.fileno(),select.EPOLLIN)
    epoll.register(sys.stdin.fileno(),select.EPOLLIN)
    while True:
        events = epoll.poll(-1)
        for fd, event in events:
            if fd == c.fileno():
                data = c.recv(100)
                if data:
                    print(data.decode('utf8'))
                else:
                    print('对方断开了')
                    return
            elif fd == sys.stdin.fileno():
                data = input()
                c.send(data.encode('utf8'))
    c.close()

if __name__ == '__main__':
    tcp_client()

