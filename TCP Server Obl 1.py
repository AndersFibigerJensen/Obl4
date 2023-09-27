from socket import *
import threading
import re
import random
import json

def handling(connectionsocket,address):
    while True:
        sentence= connectionSocket.recv(1024).decode()
        if re.search("Random;[0-9]+;[0-9]+",sentence):
            sentence=re.search("Random;[0-9]+;[0-9]+",sentence).group()
            numbers= re.findall("[0-9]+",sentence)
            sentence= str(random.randint(int(numbers[0]),int(numbers[1])))
        elif re.search("Add;[0-9]+;[0-9]+",sentence):
            sentence=re.search("Add;[0-9]+;[0-9]+",sentence).group()
            numbers= re.findall("[0-9]+",sentence)
            sentence= str(int(numbers[0])+int(numbers[1]))
        elif re.search("Subtract;[0-9]+;[0-9]+",sentence):
            sentence=re.search("Subtract;[0-9]+;[0-9]+",sentence).group()
            numbers= re.findall("[0-9]+",sentence)
            sentence= int(numbers[1])-int(numbers[0])
            sentence=str(sentence)
        elif(sentence.strip()=="quit"):
            connectionSocket.close()
            break
        connectionSocket.send(sentence.encode())

ServerName="localhost"
Serverport=2000
Serversocket=socket(AF_INET,SOCK_STREAM)
Serversocket.bind(('',Serverport))
Serversocket.listen(1)
print("Server is ready to listen")
while True:
    connectionSocket, addr= Serversocket.accept()
    threading.Thread(target=handling, args=(connectionSocket,addr)).start()

