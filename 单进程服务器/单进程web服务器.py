import re
import socket

def service(new_socket):
    request = new_socket.recv(4096).decode("utf8")
    print(request)
    request_lines = request.splitlines()
    if request_lines:
        file_name=""
        ret= re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret :
            file_name = ret.group(1)
            print("*" * 50, file_name)
            if file_name == "/":
                file_name = "/index.html"

        try:
            f = open("./html" + file_name, "rb")
        except:
            response = "HTTP/1.1 404 NOT FOUND\r\n"
            response += "\r\n"
            response += "------file not found-----"
            new_socket.send(response.encode("utf-8"))
        else:
            html_content = f.read()
            f.close()
            response = "HTTP/1.1 200 OK\r\n"
            response += "\r\n"
            new_socket.send(response.encode("utf-8"))
            new_socket.send(html_content)
    new_socket.close()





def client_connect():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('',7890))
    server.listen(128)
    while True:
        new_socket,client_addr = server.accept()
        service(new_socket)
    server.close()




if __name__ == '__main__':
    client_connect()
