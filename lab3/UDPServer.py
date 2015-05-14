# -*- utf-8 -*-

from socket import*
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive"
while 1:
    message, clientAdress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode('UTF-8').upper().encode('UTF-8')   
    serverSocket.sendto(modifiedMessage, clientAdress)
