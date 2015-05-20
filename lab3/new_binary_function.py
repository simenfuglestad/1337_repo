# -*- encoding: utf8 -*-

def charToBin(character):
    
    output = ""
    
    for c in character:
        n = ord(c)
        b = "{0:0b}".format(n)
        output += b
    print output    
    return output
            
def binToChar(binary_string):
    result = ('%x' % int(binary_string, 2)).decode('hex')
    return result


assert charToBin("å") == '1100001110100101'
charToBin("a")    
print binToChar(charToBin('an'))    
print binToChar(charToBin('æ'))
print binToChar(charToBin('å'))
