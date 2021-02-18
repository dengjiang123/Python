import socket

s=socket.socket()

host=socket.gethostname()
port=2222
s.bind((host,port))
s.listen()
while True:
    c,addr=s.accept()
    print("Got connection from: ",addr)
    str="thank you for connecting"
    str=str.encode()
    c.send(str)
    c.close()
