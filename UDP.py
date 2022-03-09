import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = ('',2000)
s.bind(addr)
data , clent_addr = s.recvfrom(50)
print(data.decode('utf8'))
s.sendto('fine'.encode('utf8'),clent_addr)
s.close()