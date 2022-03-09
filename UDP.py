<<<<<<< HEAD
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = ('',2000)
s.bind(addr)
data , clent_addr = s.recvfrom(50)
print(data.decode('utf8'))
s.sendto('fine'.encode('utf8'),clent_addr)
=======
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = ('',2000)
s.bind(addr)
data , clent_addr = s.recvfrom(50)
print(data.decode('utf8'))
s.sendto('fine'.encode('utf8'),clent_addr)
>>>>>>> e2c43e045d170dddd8b48902e123096581e081ef
s.close()