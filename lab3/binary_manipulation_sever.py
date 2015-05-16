# -*-encoding: utf-8 -*-

# Convert any number of characters to binary format. Returns a list of
# the formatted characters. Note that double byte characters are split in the
# list.
def charToBin(character):
    
    output = []
    
    for c in character:
        n = ord(c)
        b = "{0:0b}".format(n)
        output.append(b)   
    return output

# Checks a list of given binaries to see if any are in the 2-byte area of
# utf-8 and then changes the bit that determines upper/lower-case in each
# byte. If any bytes that starts with '11' is found the byte itself and the
# next byte in the list are replaced entirely with a new binary string that
# make up the two bytes.
def flipBits(binaries):

    for c in binaries[:-1]:
        if len(list(c)) == 8:
            temp = c
            if temp[0] == "1" and temp[1] == "1":
                temp = c + binaries[binaries.index(c) + 1]
                binaries.insert(binaries.index(c), temp)
                binaries.remove(binaries[binaries.index(c) + 1])
                binaries.remove(c)
    
    outlist = []
             
    for b in binaries:
        if 17 > len(list(b)) > 7:
            b = list(b)
            if b[10] == '0':
                b[10] = '1'
            elif b[10] == '1':
                b[10] = '0'     
            b = ''.join(b)
            outlist.append(b)
            
        elif len(list(b)) == 7 :
            b = list(b)
            if b[1] == '0':
                b[1] = '1'
            elif b[1] == '1':
                b[1] = '0'
            b = ''.join(b)
            outlist.append(b)
        else:
            print "Uknown symbol"
            print "Exiting..."
            exit(0)
            
    return outlist
    
# Convert a list of binaries to characters and returns them as a string.
# The conversion is done by summing up the binary, get the hexadecimal
# value from the sum and decode with hexadecimal.
def binToChar(binary_list):
    result = ""
    for c in binary_list:
        result += ('%x' % int(c, 2)).decode('hex')
    return result

# Testing that all functions behave after expectations
def test():
    assert charToBin("a") == ['1100001']
    assert charToBin("A") == ['1000001']
    assert charToBin("å") == ['11000011', '10100101']
    assert charToBin("Å") == ['11000011', '10000101']
    assert flipBits(['1100001']) == ['1000001']
    assert flipBits(['1000001']) == ['1100001']
    assert flipBits(['11000011', '10100101']) == ['1100001110000101']
    assert binToChar(['1100001']) == 'a'
    assert binToChar(['1000001']) == 'A'
    assert binToChar(['1100001110100101']) == 'å'
    assert binToChar(['1100001110000101']) == 'Å'
    return "All tests completed, program running normally"

# Import all data from the socket module, set up a serverport and bind it to a 
# socket. 
from socket import*
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

# Starts a while loop so that the program is always ready to recieve a message.
# Inside the loop checks if input is 'quit' to determine continuation.
print "The server is ready to receive"
print "If you wish to exit, type 'quit'"
while 1:
    message, clientAdress = serverSocket.recvfrom(2048) # Where to get message
    print message
    if message == "quit":
        print "Quitting..."
        exit(1)
    new_message = binToChar(flipBits(charToBin(message))) # The conversion
    serverSocket.sendto(new_message, clientAdress) # Send the message back
    serverSocket.sendto(test(), clientAdress)
