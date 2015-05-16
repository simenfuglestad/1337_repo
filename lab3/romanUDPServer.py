# -*- utf-8 -*-
# import json, needed to deserialize the message from the client
# import all functions from socket
# import the inspect module, we will use this to determine function call
# import all function from our custom roman module 'roman.py'
import json
import inspect
from roman import *
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

# This dictionary is used to identify the 'tags' contained in the message
# from the client and associate them with a method call. The methods are from
# our roman.py module.

action_dict = {
    'DTR': to_roman,
    'RTD': from_roman,
    'ADD': add_roman,
    'SUB': subtract_roman,
    'MUL': multiply_roman,
    'DIV': divide_roman
    }

# Alert user that server is ready to recieve and begin a while loop that will
# not terminate unless shut down with terminal commands. Inside the loop we
# listen for a message from the client then and deserialize it with json. After
# this we loop over all elemtents in the message except the last one(where the
# tag is) and convert them to integer if any string digits are found. Then 
# another loop scanes the message for a tag to match one in action_dict. If a
# tag is found then the value function of that key is called. Also note that we
# use the inspect module here to determine if the function requires one or two
# paramteres. The paramteres themselves are contained in the message. Finaly
# note that if the paramteres are not integers then they are encoded to ascii.
# The reason for this is that json.loads gives us unicode strings, which will
# not be accepted for sending over the serversocket. 
print "The server is ready to receive"
while 1:
    message, clientAdress = serverSocket.recvfrom(2048)
    print message
    message = json.loads(message)
    modified_message = ""
    for c in message[:-1]:
        if c.isdigit():
            n = int(c)
            message.insert(message.index(c), n)
            message.remove(c)
    for k, v in action_dict.iteritems():
        if k in message:
            if len(inspect.getargspec(v)[0]) == 1:
                if not isinstance(message[0], int):
                    roman_param = message[0].encode('ascii')
                modified_message = v(roman_param)
            elif len(inspect.getargspec(v)[0]) == 2:
                if not isinstance(message[0], int):
                    roman_param1 = message[0].encode('ascii')
                    roman_param2 = message[1].encode('ascii')
                modified_message = v(roman_param1, roman_param2)
            else:
                print "Unexpected error, cannot complete operation"
                print "Exiting..."
                exit(1)
    
    # Make sure we are sending back string, relevant for decimal conversion
    modified_message = str(modified_message)
    
    # Send the message back to client.
    serverSocket.sendto(modified_message, clientAdress)
