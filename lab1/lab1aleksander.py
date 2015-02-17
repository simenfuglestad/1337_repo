# -*- coding: utf8 -*-

#
# IS-105 LAB1
#

# Import librarys to get different functions.
import sys
import psutil

# Alle gruppemedlemmene

gruppe = {  'student1': 'Simen Tokerud',
            'student2': 'Andreas Ougland',
            'student3': 'Simen Fuglestad',
            'student4': 'Stefan Blomberg',
            'student5': 'Aleksander Aspevik',
            'student6': 'Jørgen Haraldseid Gramstad'
}

# Oppgave 1

# Function that prints out a bird
def ascii_bird():
	bird = """
	       \/_
	  \,   /( ,/
	   \\\' ///
	    (./
	     '`
 	    """ 
	print(bird)

# Runs the function and prints out the bird
ascii_bird()


# Oppgave 2

# Function that does a bitwise AND operation on two numbers.
# Returns the result
def bitAnd(x, y):
	return x & y


# Oppgave 3

# Function that does a bitwise XOR operation on two numbers.
# Returns the result.
def bitXor(x, y):
	return x ^ y

# Oppgave 4

# Function that does a bitwise OR operation on two numbers and returns the result
def bitOr(x, y):
	return x | y


# Oppgave 5

# Function that takes a letter, transforms it into to decimal number and then
# turns it into a bit-number.
def ascii8Bin(letter):
	result = ord(letter)
	return '{0:08b}'.format(result)


# Oppgave 6 

def transferBin(string): 
	l = list(string)
	binaries = ""
	for c in l:
		# skriv ut den binære representasjon av hvert tegn (bruk ascii8Bin funksjonen din)
		result = ascii8Bin(c)
		binaries += result + '\n'
	return binaries
	

# Oppave 7

def transferHex(string):
	l = list(string)
	hexes = ""
	for c in l:
		result = hex(ord(c))
		hexes += result + '\n'
	return hexes

# Oppgave 8


def unicodeBin(character):
    conv = unicode(character, 'UTF-8')
    return ascii8Bin(conv)    
    
# Oppgave 9

# Tilgjengelighet avhenger av root user. Kan hente info fra prosesser som kjører fra din brukers tilgang.
# Mange (de fleste operativsystemer) gjemmer info om seg selv.
# PSutil kan finne harddrive capacity, minne (RAM), antall CPUer.



def printSysInfo():
    cpu = psutil.NUM_CPUS
    memory = psutil.virtual_memory().total
    disk = psutil.disk_usage('/').total
    
    specs = [cpu, memory, disk]
    
    return specs
    


def sysInfoTest():
    cpu = psutil.NUM_CPUS
    memory = psutil.virtual_memory().total
    disk = psutil.disk_usage('/').total
    
    assert printSysInfo() == [cpu, memory, disk]
    return "test completed"


def test():
	assert bitAnd(6, 5) == 4
	assert bitXor(4, 5) == 1
	assert bitOr(0, 1) == 1
	assert ascii8Bin('a') == '01100001'
	assert ascii8Bin('A') == '01000001'
	assert transferBin('Hi') == "01001000\n01101001\n"
	assert transferHex('Hei') == "0x48\n0x65\n0x69\n"				
	assert unicodeBin('å') == '11100101'
	# Dine egne tester
	return "Testene er fullført uten feil."


# Bruk denne funksjonen for å vise at alle testene er kjørt feilfritt
print test()
