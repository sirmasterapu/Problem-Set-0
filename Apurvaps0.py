
def odd_or_even(number):
	'''Checks if Number is odd or even'''
	evenodd = number % 2#A number divisible by two is even, so if their is no remainder it means two is a factor meaning its even
	
	if evenodd > 0:
		return False
	
	else:
		return True
	
	
 
def length(number):
	'''Returns the length of number'''
	count = 0
	programOn = True
	standard1 = 1
	standard10 = 10
	
	if number == 0:
		return 0
		
	while programOn:
		count += 1
			
		if standard10 > number >= standard1:#Tests its digit length e.g. between 1- 10 is 1 digit etc.
			return count
			programOn = False
			
		else:
			standard1 = standard1 * 10#Continuously changes the placeholder area to test how many digits are in it
			standard10 = standard10 * 10
				
		
	
	
def sum_of_less_digits(digit):
	'''Gets the sum of the digits less than the original digit'''
	sum = 0
	for item in range(digit):#Range is all the numbers less than the number, so adding them individually
		sum += item
	
	return sum

def sum_of_digits(number):
	'''Adds the digits in any number'''
	sum = 0
	
	while number > 0:
		singleDigit = number % 10#Gets the first digit
		number = number - singleDigit# Gets the original number first digit place to 0
		sum = sum + singleDigit# Adds the first digit of the number
		number = number / 10# Because the original first number is now 0 dividing it by 10 makes the next first digit the one from the tens value
		
	return sum

def factorial(number):
	'''Gets the factorial of a given number'''
	factorial = 1
	for item in range(1,number + 1):#Cant just be range(number) otherwise it would multiply by 0
		factorial *= item
	
	return factorial

def factoring(number, factor):
	'''Tells whether or not a the chosen number is a factor of the other number'''
	if factor == 0:
		return False
		
	else:	
		remainder = number % factor# factors dont have remainders
		
		if remainder > 0:
			return False
			
		else:
			return True

def prime(number):
	"""This function checks if the argument is prime"""
	count = 2 #start count at 2 because 1 is a factor of every number
	while count != number:
 		remainder = number % count # constantly increments to check all numbers below if they are factors
 		
 		if remainder == 0:
 			return False
 			
 		else:
 			count += 1
 	return True
 			
def perfect(number):

	"""This function checks if the argument is a perfect number"""
	
	factorTotal = 0 #keeps track of the factors
	count = 1
	while count != number:
 			if number % count == 0:#factoring
 				factorTotal += count#Adds the factors
 			count += 1
 			
	if factorTotal == number:# Checks if the added factors make the number
		return True
	else:
		return False

def sum_div(number):
	'''checks if the sum of the digits of a number is a factor of the original number'''
	total = sum_of_digits(number)#Other Function
	remainder = number % total#Factoring
	if remainder == 0:
		return True
	else:
		return False
	
	
 			