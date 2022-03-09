import socket
import select
import sys

def tcp_client():
    if len(sys.argv) == 1:
        return
    else:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest_addr = (sys.argv[1], 2000)
        client.connect(dest_addr)
        epoll = select.epoll()
        epoll.register(client.fileno(), select.EPOLLIN)
        epoll.register(sys.stdin.fileno(), select.EPOLLIN)
        while True:
            events = epoll.poll(-1)
            for fd, event in events:
                if fd == client.fileno():
                    data = client.recv(100)
                    if data:
                        print(data.decode('utf8'))
                    else:
                        print('对方断开了')
                        return
                elif fd == sys.stdin.fileno():
                    data = input()
                    client.send(data.encode('utf8'))

    client.close()

if __name__ == '__main__':
    tcp_client()