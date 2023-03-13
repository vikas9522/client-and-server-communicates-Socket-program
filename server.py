import socket
s=socket.socket()
print("socket created successfully ")

s.bind(('localhost',54321))

s.listen(3)
print("waiting for the connections")

while True:
    c,addr= s.accept()
    name=c.recv(1024).decode()
    print("connected with",addr,name)
    response=input(str("enter your message :"))
    c.send(bytes(response,"utf-8"))
    # c.send(bytes('welcome to vikas tomar page','utf-8'))
    c.send(bytes('bye','utf-8'))
    end=c.recv(1024).decode()
    print(" last recieved from client :",end)
    c.close()