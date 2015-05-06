# -*-encoding: utf-8 -*-
import json

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
    
def getInput():
    done = False
    output_list = []
    while not done:
        user_input = raw_input("Enter letter: ")
        if not user_input:
            done = True
        else:
            output_list.append(user_input)
    return output_list
        


def flipBit(text):
    text = list(text)
    binary_list = []
    for c in text:
        u = c.encode('utf-8')
        binary_list.append(unicodeBin(u))
        
    output_list = []
    for b in binary_list:
        if len(b) > 8:
            b = list(b)
            print "2 bytes"
            
            if b[10] == '0':
                b[10] = '1'
            elif b[10] == '1':
                b[10] = '0'
            b = ''.join(b)
            output_list.append(b)         
            
        else:
            print "1 byte"
            b = list(b)
            
            if b[2] == '0':
                b[2] = '1'
            elif b[2] == '1':
                b[2] = '0'
            b = ''.join(b)
            output_list.append(b)
            
    output = ''.join(output_list)
    return output
            
def binaryToCharacter(binary_string):
    result = ('%x' % int(binary_string, 2)).decode('hex')
    return result


from socket import*
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive"
while 1:
    message, clientAdress = serverSocket.recvfrom(2048)
    print message
    message = json.loads(message)
    flip = flipBit(message)
    message = binaryToCharacter(flip)
    serverSocket.sendto(message, clientAdress)    

