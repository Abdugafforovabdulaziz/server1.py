#qurbon
import socket
import datetime
def displaytime():
    now = datetime.datetime.now()
    return ("["+now.strftime("%Y-%m-%d %H:%M:%S") +"]")

server = socket.socket()

host = '127.0.0.1'
port = 1234

server.connect((host, port))

run = True

while run :

    msg = server.recv(10053)
    print(displaytime(),msg.decode('UTF-8'))

    server.send('Qurbon online holatda!'.encode('UTF-8'))