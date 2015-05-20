# -*- utf-8 -*-

# import the json module to make list transfer over sockets possible
# importing functions from the socket module
import json
from socket import *

# The client will send to localhost IP
# Selecting serverport. Port number must not be in use.
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# list to be used in following algorithm to determine legal/illegal input

valid_numerals = ['I','V', 'X', 'L', 'C', 'D' 'M']

# This function uses a step-by-step algorithm to ensure that the user does not
# enter illegal commands for the server to handle. The same basic structure is 
# used for each of the 6 possible inputs with a few exceptions for each. Such 
# exceptions include when the desired function requires two paramters intead 
# of one or for decimal converion where we need to check for valid integer.
# In addition to returning the user input as a list, the list in question also
# contains a 'tag', a string added by the program. This tag is unique for all
# the different actions and will assist the server in determining which
# operation to perform.
def get_input():
    print "Welcome to 1337's Roman Client!\n"
    print "Below are your avaialble actions:"
    print "1. Convert decimal to Roman"
    print "2. Convert Roman to decimal"
    print "3. Add Roman numbers"
    print "4. Subtract Roman numbers"
    print "5. Multiply Roman numbers"
    print "6. Divide Roman numbers"
    user_input = raw_input('\nSelect action by pressing a number 1-6: ')
    
    if user_input.isdigit():
        if user_input == "1":
            number = raw_input("Enter decimal to convert to Roman: ")
            if number.isdigit():
                return [number, "DTR"]
            else:
                print "You must enter a valid decimal number"
                print "Exiting..."
                exit(0)
                
        elif user_input == "2":
            numeral_input = raw_input ("Enter Roman numeral to convert: ")
            numeral_input = numeral_input.upper()
            for c in numeral_input:
                if c not in valid_numerals:
                    print "Must enter only valid numerals"
                    print "Exiting..."
                    exit(0)
            return [numeral_input, "RTD"]
            
        elif user_input == "3":
            print "Enter 2 Roman numerals to add together"
            numeral_1 = raw_input("First numeral here: ")
            numeral_1 = numeral_1.upper()
            print numeral_1
            
            for c in numeral_1:
                if c not in valid_numerals:
                    print "Must enter only valid numerals"
                    print "Exiting..."
                    exit(0)
            numeral_2 = raw_input("\nSecond numeral here: ")
            numeral_2 = numeral_2.upper()
            
            for c in numeral_2:
                if c not in valid_numerals:
                    print "Must enter only valid numerals"
                    print "Exiting..."
                    exit(0)
            return [numeral_1, numeral_2, 'ADD']
            
        elif user_input == "4":
            print "Enter 2 Roman numerals to subtract."
            numeral_1 = raw_input("First numeral here: ")
            numeral_1 = numeral_1.upper()
            
            for c in numeral_1:
                if c not in valid_numerals:
                    print "Must enter only valid numerals"
                    print "Exiting..."
                    exit(0)
            numeral_2 = raw_input("\nSecond numeral here: ")
            numeral_2 = numeral_2.upper()
            
            for c in numeral_2:
                if c not in valid_numerals:
                    print "Must enter only valid numerals"
                    print "Exiting..."
                    exit(0)
            return [numeral_1, numeral_2, 'SUB']

        elif user_input == "5":
            print "Enter 2 Roman numerals to multiply"
            numeral_1 = raw_input("First numeral here: ")
            numeral_1 = numeral_1.upper()
            
            for c in numeral_1:
                if c not in valid_numerals:
                    print "Must enter only valid numerals"
                    print "Exiting..."
                    exit(0)
            numeral_2 = raw_input("\nSecond numeral here: ")
            numeral_2 = numeral_2.upper()
            
            for c in numeral_2:
                if c not in valid_numerals:
                    print "Must enter only valid numerals"
                    print "Exiting..."
                    exit(0)
            return [numeral_1, numeral_2, 'MUL']
            
        elif user_input == "6":
            print "Enter 2 Roman numerals to divide"
            numeral_1 = raw_input("First numeral here: ")
            numeral_1 = numeral_1.upper()
            
            for c in numeral_1:
                if c not in valid_numerals:
                    print "Must enter only valid numerals"
                    print "Exiting..."
                    exit(0)
            numeral_2 = raw_input("\nSecond numeral here: ")
            numeral_2 = numeral_2.upper()
            
            for c in numeral_2:
                if c not in valid_numerals:
                    print "Must enter only valid numerals"
                    print "Exiting..."
                    exit(0)
            return [numeral_1, numeral_2, 'DIV']
    else:
        print "Must enter a number between 1-6"
        print "Exiting..."
        exit(0)

# Get string from user input and serialize it with json. Note that we do this
# because the object we are going to send is a list which is not accepted by 
# default.             
message = get_input()
message = json.dumps(message)           

# Send the message to the server socket with specified port                         
clientSocket.sendto(message,(serverName, serverPort))
# Listen to server for modified message and then print it
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print "The result is %s" % modifiedMessage
# Close the client socket, the apllication is finished
clientSocket.close()
