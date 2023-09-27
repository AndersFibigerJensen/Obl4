from  socket import *

Servername="localhost"
Serverport=2000
clientsocket=socket(AF_INET,SOCK_STREAM)
clientsocket.connect((Servername,Serverport))
sentence=""
while sentence !="quit":
    sentence=input("please enter a sentence ")
    clientsocket.send(sentence.encode())
    modifiedsentence=clientsocket.recv(1024)
    print("from server: " + modifiedsentence.decode())
clientsocket.close()