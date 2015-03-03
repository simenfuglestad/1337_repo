# -*- coding: utf8 -*-

#Try the .read(1) in here somwhere...
import sys
import struct

def convertStringToBinary():
   
    text = raw_input("Enter a string > ")
    byte_text = bytearray(text).decode("UTF-8")
    
    for c in byte_text:
        
        unpacked = struct.unpack('b', c)[0]
        binaries = '{0:08b}'.format(unpacked)
        print binaries
        
convertStringToBinary()

def convertStringToBinary2():
    
    text = raw_input("Enter a string > ")
    byte_text = bytearray(text).decode("UTF-8")    
    print byte_text
    
    for c in byte_text:
        print len(c)
       
        if len(c) > 1:
            print "test"
            unpacked = struct.unpack('2b', c)[0]
            binaries = '{0:08b}'.format(unpacked)
            print binaries
            
        else:
            print "test 2"
            unpacked = struct.unpack('b', c)[0]
            binaries = '{0:08b}'.format(unpacked)
            print binaries
            
            
#convertStringToBinary2()


