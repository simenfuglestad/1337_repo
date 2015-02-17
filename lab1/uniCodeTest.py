# -*- coding: utf8 -*-

def ascii8Bin(letter):
	result = ord(letter)
	return '{0:08b}'.format(letter)



def unicodeBin(character):
    conv = unicode(character, 'UTF-8')
    return ascii8Bin(conv)


def unicodeBin2(character):
    result = bytearray(character)
    string = ""
    for c in result:
        c = unicode(character, 'UTF-8')
        string += string + c
    return ascii8Bin(result)


print unicodeBin2("å")

