import socket
c= socket.socket()

c.connect(('localhost',54321))


name=input(str("enter your message :"))
c.send(bytes(name,"utf-8"))
print(c.recv(1024).decode())
end=input(str("enter your message :"))
print(c.recv(1024).decode())
c.send(bytes(end,"utf-8"))

