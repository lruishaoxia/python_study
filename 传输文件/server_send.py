<<<<<<< HEAD
from socket import *
import struct
def tcp_init():
    s = socket(AF_INET, SOCK_STREAM)
    addr = ('', 2000)
    s.bind(addr)
    s.listen(128)
    return s

def send_file():
    file_name = 'file1'
    s = tcp_init()
    new_client, client_addr = s.accept()
    file_name_bytes = file_name.encode('utf8')
    train_head_bytes = struct.pack('I', len(file_name_bytes))
    new_client.send(train_head_bytes + file_name_bytes)
    f = open(file_name, 'rb')
    file_content = f.read()
    train_head_bytes = struct.pack('I', len(file_content))
    new_client.send(train_head_bytes + file_content)
    f.close()
    new_client.close()
    s.close()

if __name__ == '__main__':
=======
from socket import *
import struct
def tcp_init():
    s = socket(AF_INET, SOCK_STREAM)
    addr = ('', 2000)
    s.bind(addr)
    s.listen(128)
    return s

def send_file():
    file_name = 'file1'
    s = tcp_init()
    new_client, client_addr = s.accept()
    file_name_bytes = file_name.encode('utf8')
    train_head_bytes = struct.pack('I', len(file_name_bytes))
    new_client.send(train_head_bytes + file_name_bytes)
    f = open(file_name, 'rb')
    file_content = f.read()
    train_head_bytes = struct.pack('I', len(file_content))
    new_client.send(train_head_bytes + file_content)
    f.close()
    new_client.close()
    s.close()

if __name__ == '__main__':
>>>>>>> e2c43e045d170dddd8b48902e123096581e081ef
    send_file()