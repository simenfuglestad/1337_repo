# -*- utf-8 -*-
#from binascii import *

def ascii8Bin(letter):
	result = ord(letter)
	return '{0:08b}'.format(result)

def unicodeBin(character):

    outstr = ""
    unicode_char = bytearray(character)
    
    if len(unicode_char) > 1:
        for char in bytearray(unicode_char):
            outstr += "{0:08b} ".format(char)
    
    else:
        outstr = "{0:08b}".format(ord(character))
    
    outstr = outstr.replace(" ", "")
    return outstr.encode('utf_8')

from socket import*
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive"
while 1:
    message, clientAdress = serverSocket.recvfrom(2048)
    #modifiedMessage = message.upper()
    #modifiedMessage = message.decode('UTF-8').upper().encode('UTF-8')
    temp = []
    for c in message:
        binary_list = list(unicodeBin(c))
        if binary_list[2] == '1':
            binary_list[2] = '0'
        elif binary_list[2] == '0':
            binary_list[2] == '1'
        binary_list = ''.join(binary_list)
        print binary_list
        
        temp.append(binary_list)
    print temp
    result = []
    for b in temp:
        b = int(b, 2)
        result.append(unichr(b))
        print unichr(b)
    print result
    serverSocket.sendto(message, clientAdress)
    
    
