from socket import*
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive"
while 1:
    message, clientAdress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode('utf-8').upper().encode('utf-8')
    serverSocket.sendto(modifiedMessage, clientAdress)
