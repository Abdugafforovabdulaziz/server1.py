#server 
import socket
import datetime
def displaytime():
    now = datetime.now()
    return("["+now.strftime("%Y-%m-%d %H:%M:%S")+"]")

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host =     '127.0.0.1'
port = 1234
server.bind((host, port))
server.listen(5)
Client,addr = server.accept()
print(displaytime(),'Qurbon kompyuteri boglandi',addr)
run = True
while run:

    try:

        date = input(">>>")
        client.send(date.encode('UTF-8'))

    except ConnectionResetError:

        print(displaytime(),'Qurbon tarmoqdan uzildi...>> boglanishga harakat qilinyapti...') 
        client,addr = server.accept()
        print(displaytime(),'Qurbonboglani >>>',addr)
