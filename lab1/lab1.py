# -*- coding: utf8 -*-

#
# IS-105 LAB1
#

# Import librarys to get different functions.
import sys  # Import functions from the sys library.
import psutil  # Import functions from the psutil library.

# All groupmembers in the 1337 group.
gruppe = {  'student1': 'Simen Tokerud',  # Creates a group of students in a dictonary.
            'student2': 'Andreas Ougland',
            'student3': 'Simen Fuglestad',
            'student4': 'Stefan Blomberg',
            'student5': 'Aleksander Aspevik',
            'student6': 'Jørgen Haraldseid Gramstad'
}


# Assignment 1

# Function that prints out an ascii-bird
def ascii_bird():  # Creates the definition aschii_bird.
	bird = """
	       \/_
	  \,   /( ,/
	   \\\' ///
	    (./
	     '`
 	    """ 
	print(bird)  # Prints the variable bird.

# Runs the function and prints out the bird.
ascii_bird()


# Assignment 2

# Function that does a bitwise AND operation on two numbers.
# Returns the result
def bitAnd(x, y):
	return x & y


# Assignment 3

# Function that does a bitwise XOR operation on two numbers.
# Returns the result.
def bitXor(x, y):
	return x ^ y


# Assignment 4

# Function that does a bitwise OR operation on two numbers and returns the result
def bitOr(x, y):
	return x | y


# Assignment 5

# Function that takes a letter, transforms it into to decimal number and then
# turns it into a bit-number.
def ascii8Bin(letter):
	result = ord(letter)
	return '{0:08b}'.format(result)


# Assignment 6 

def transferBin(string): 
	l = list(string)  # Creates a list named "l" wich consists of strings.
	binaries = ""
	for c in l:  # Print the binary representation of each character. (use your ascii8Bin function)
		result = ascii8Bin(c)
		binaries += result + '\n'
	return binaries
	

# Assignment 7

def transferHex(string):
	l = list(string)
	hexes = ""
	for c in l:
		result = hex(ord(c))
		hexes += result + '\n'
	return hexes


# Assingment 8

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
    
    
# Assignment 9

# Availability depends on the root user. Can retrieve info from processes running from your user's access.
# Most operating systems hides information about themselves.
# PSUtils can find hard drive capacity, memory (RAM), number of CPUs and so on.

# A function to check the status of the CPU, virtual memory and disk(s) you have on your computer.
def printSysInfo():
    cpu = psutil.NUM_CPUS
    memory = psutil.virtual_memory().total
    disk = psutil.disk_usage('/').total
    
    specs = [cpu, memory, disk]
    
    return specs
    

# Tests   
    
# A test to check the status of the CPU, virtual memory and disk(s) on your computer.
def sysInfoTest():
    cpu = psutil.NUM_CPUS
    memory = psutil.virtual_memory().total
    disk = psutil.disk_usage('/').total
    
    assert printSysInfo() == [cpu, memory, disk]
    return "test completed"


# Some tests to check if things work as planned.
def test():
	assert bitAnd(6, 5) == 4
	assert bitXor(4, 5) == 1
	assert bitOr(0, 1) == 1
	assert ascii8Bin('a') == '01100001'
	assert ascii8Bin('A') == '01000001'
	assert transferBin('Hi') == "01001000\n01101001\n"
	assert transferHex('Hei') == "0x48\n0x65\n0x69\n"				
	assert unicodeBin('å') == '11000011 10100101'
	# Your own tests.
	return "Testene er fullført uten feil."


# Use this function to check that all the tests returns no errors.
print test()
