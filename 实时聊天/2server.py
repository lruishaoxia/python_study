<<<<<<< HEAD
import  socket
import select
import sys

def tcp_server():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr=('',2000)
    s.bind(addr)
    s.listen(128)
    new_server, client_addr=s.accept()
    epoll = select.epoll()
    epoll.register(new_server.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(),select.EPOLLIN)
    while True:
        events = epoll.poll(-1)
        for fd,event in events:
            if fd == new_server.fileno():
                data = new_server.recv(100)
                if data :
                    print(data.decode('utf8'))
                else:
                    print('对方已离开')
                    return

            elif fd == sys.stdin.fileno():
                try:
                    data= input()
                except EOFError:
                    print('886')
                    return
                new_server.send(data.encode('utf8'))

    new_server.close()
    s.close()

if __name__ == '__main__':
    tcp_server()


=======
import  socket
import select
import sys

def tcp_server():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr=('',2000)
    s.bind(addr)
    s.listen(128)
    new_server, client_addr=s.accept()
    epoll = select.epoll()
    epoll.register(new_server.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(),select.EPOLLIN)
    while True:
        events = epoll.poll(-1)
        for fd,event in events:
            if fd == new_server.fileno():
                data = new_server.recv(100)
                if data :
                    print(data.decode('utf8'))
                else:
                    print('对方已离开')
                    return

            elif fd == sys.stdin.fileno():
                try:
                    data= input()
                except EOFError:
                    print('886')
                    return
                new_server.send(data.encode('utf8'))

    new_server.close()
    s.close()

if __name__ == '__main__':
    tcp_server()


>>>>>>> e2c43e045d170dddd8b48902e123096581e081ef
