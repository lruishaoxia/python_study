from socket import *
import struct

tcp_client_socket = socket(AF_INET, SOCK_STREAM)
address = ('192.168.5.2', 2000)
tcp_client_socket.connect(address)
train_head_bytes = tcp_client_socket.recv(4)
train_content_len = struct.unpack('I', train_head_bytes)
file_name = tcp_client_socket.recv(train_content_len[0])
f = open(file_name.decode('utf8'), 'wb')
train_head_bytes = tcp_client_socket.recv(4)
train_content_len = struct.unpack('I', train_head_bytes)
file_content = tcp_client_socket.recv(train_content_len[0])
f.write(file_content)
f.close()
tcp_client_socket.close()
