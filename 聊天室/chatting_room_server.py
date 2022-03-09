import socket
import select
import sys


def tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('', 2000)
    s.bind(addr)
    s.listen(128)
    epoll = select.epoll()
    epoll.register(s.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    client_list = []
    while True:
        events = epoll.poll(-1)
        for fd, event in events:
            if fd == s.fileno():
                new_client, client_addr = s.accept()
                client_list.append(new_client)
                epoll.register(new_client.fileno(), select.EPOLLIN)
            else:
                remove_client = None
                for client in client_list:
                    if client.fileno() == fd:
                        data = client.recv(1000)
                        if data:
                            for other_client in client_list:
                                if other_client is client:
                                    pass
                                else:
                                    other_client.send(data)
                        else:
                            remove_client = client
                if remove_client:
                    client_list.remove(remove_client)
                    epoll.unregister(remove_client.fileno())
                    remove_client.close()


    s.close()


if __name__ == '__main__':
    tcp_server()