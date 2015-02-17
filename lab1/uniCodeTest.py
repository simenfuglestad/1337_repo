# -*- coding: utf8 -*-

def ascii8Bin(letter):
	result = ord(letter)
	return '{0:08b}'.format(letter)

def unicodeBin(character):

    outstr = ""
    unicode_char = bytearray(character)
    
    if len(unicode_char) > 1:
        for char in bytearray(unicode_char):
            outstr += "{0:08b} ".format(char)
    
    else:
        outstr = "{0:08b}".format(ord(character))
    
    return outstr


print unicodeBin("å")


