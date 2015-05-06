# -*-coding: utf-8 -*-
#from binascii import *

def unicodeBin(character):

    outstr = ""
    unicode_char = bytearray(character)
    
    if len(unicode_char) > 1:
        for char in bytearray(unicode_char):
            outstr += "{0:08b} ".format(char)
    
    else:
        outstr = "{0:08b}".format(ord(character))
    
    outstr = outstr.replace(" ", "")
    return outstr

from socket import*
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive"
while 1:
    message, clientAdress = serverSocket.recvfrom(2048)
    #modifiedMessage = message.upper()
    #modifiedMessage = message.decode('UTF-8').upper().encode('UTF-8')
    
    result = ('%x' % int(result, 2)).decode('hex')
    
    serverSocket.sendto(message, clientAdress)
    
