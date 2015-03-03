# -*- coding: utf-8 -*-

# Roman multiplication

# 1. For hver gang det venstre tallet halveres dobles tallet på høyre side.
# 2. Legge sammen alle tall som når halveres er et oddetall.

# Checks to see if the inserted number is an odd or even number
def check_odd(x):
	if x % 2 == 1: # if the number leaves a remainder then the number is odd
		return True
	else:
		return False



# function that multiplies two numbers
def roman_multiplication(x, y):
	valid_nums = [] # list for keeping the numbers to be added
	
	result = float(y)/2
		
	while x >= 1: # when 1 is reached the loop terminates
			
		result += result
		if check_odd(x) == True:
			valid_nums.append(result)
#			print valid_nums
			x /= 2
		else:
			x /= 2
		
	final_result = 0
	for i in range(len(valid_nums)):
		final_result += valid_nums.pop()
#	print(final_result)
	
	return final_result
		
# roman_multiplication(2, 3)

# tests

def tests():
	assert check_odd(1) == 1
	assert check_odd(357) == 1
	assert check_odd(44) == 0
	assert check_odd(8) == 0
	assert roman_multiplication(9, 3) == 27
	assert roman_multiplication(15, 22) == 330.0
	assert roman_multiplication(322, 76) == 24472.0
	assert roman_multiplication(44, 78) == 3432.0
	
	return "Your tests was successful!"
	
print tests()