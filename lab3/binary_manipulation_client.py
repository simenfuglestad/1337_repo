# -*-encoding: utf-8 -*-

# Importing functions from socket, sys and the Json library

from socket import *
import json
from sys import *

# The client will send to localhost IP
# Selecting serverport. Port number must not be in use.
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Get userinput and returns it as String.

def getInput():
    user_input = raw_input("Enter a string: ");
    return user_input

# Get string from user input and send it to the server.
message = getInput()
clientSocket.sendto(message,(serverName, serverPort))

# Listen to server input and print it when it is recieved
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage

# Listen to server input and print it. Same as before except we are 
# excepting the test() call from the server.
testMessage, serverAddress = clientSocket.recvfrom(2048)
print testMessage

# Close the socket, the application is finished running
clientSocket.close()
