# -*-encoding: utf-8 -*-

from socket import *
import json
from sys import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

def getInput():
    done = False
    output_list = []
    while not done:
        user_input = raw_input("Enter character: ")
        input_list = [user_input]
        if len(input_list) > 1:
            print "Must type a single character"
            break
        elif not user_input:
            done = True
        else:
            output_list.append(user_input)
    if output_list:
        return output_list
    else:
        print "You did not enter any characters, exiting..."
        exit(0)

message = json.dumps(getInput())
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()
