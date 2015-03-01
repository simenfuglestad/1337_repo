# -*- utf-8 -*-
import re

romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))


def toRoman(n):
    n = int(n)
    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result

from socket import*
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))



print "The server is ready to receive"
while 1:
    message, clientAdress = serverSocket.recvfrom(2048)
    #modifiedMessage = message.decode('UTF-8').upper().encode('UTF-8')
    modifiedMessage = toRoman(message)
    serverSocket.sendto(modifiedMessage, clientAdress)
    
    
    
