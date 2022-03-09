<<<<<<< HEAD
# 完成TCP服务器端代码编写，客户端代码编写，客户端可以给服务器发一句话，服务器可以给客户端发一句话
import socket


def tcp_serve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('192.168.5.2', 2000)
    s.bind(addr)
    s.listen(128)
    new_client, client_addr = s.accept()
    print(client_addr)
    new_client.send('how are you'.encode('utf8'))
    data = new_client.recv(100)
    print(data.decode('utf8'))
    new_client.close()
    s.close()

    if __name__ == '__main__':
        tcp_serve()
=======
# 完成TCP服务器端代码编写，客户端代码编写，客户端可以给服务器发一句话，服务器可以给客户端发一句话
import socket


def tcp_serve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('192.168.5.2', 2000)
    s.bind(addr)
    s.listen(128)
    new_client, client_addr = s.accept()
    print(client_addr)
    new_client.send('how are you'.encode('utf8'))
    data = new_client.recv(100)
    print(data.decode('utf8'))
    new_client.close()
    s.close()

    if __name__ == '__main__':
        tcp_serve()
>>>>>>> e2c43e045d170dddd8b48902e123096581e081ef
