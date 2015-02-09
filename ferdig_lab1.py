
#-*- coding: utf-8 -*-
import psutil

gruppe = {  'student1': '-', \
			'student2': '-', \
            'student3': '-', \
            }
#Oppgave 1


def ascii_bird():
    bird = """
       \/_
  \,   /( ,/
   \\\' ///
    \_ /_/
    (./
     '` 
     """
    print bird
	
#ascii_bird()


#Oppgave 2

def bitAnd(x, y):
	return x & y
	

#Oppgave 3

def bitXor(x, y):
	return x ^ y
	


#Oppgave 4

def bitOr(x, y):
	return x | y
	
#Oppgave 5

def ascii8Bin(letter):
	conv = ord(letter)
	return '{0:08b}'.format(conv)
	
#ascii8Bin("a")


#Oppgave 6


def transferBin(string):
    l = list(string)
    #results = [ascii8Bin for c in l]
    #return '\n'.join(results)
    for c in l:
        return ascii8Bin(c)

#Oppgave 7

def transferHex(string):
	l = list(string)
	for c in l:
	    conv = ord(string)
        return '{0:06x}'.format(conv)
	    
#Oppgave 8


def unicodeBin(character):
    conv = unicode(character, 'UTF-8')
    return ascii8Bin(conv)    
    
#Oppgave 9

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
	assert transferBin('w') == '01110111'
	assert transferHex('n') == '00006e'
	assert unicodeBin('å') == '11100101'
	# Dine egne tester
	return "Testene er fullført uten feil."

print test()
#print ascii8Bin('a')
#print unicodeBin('å')
#print printSysInfo()
#print sysInfoTest()
#ascii_bird()
