
def odd_or_even(number):
	'''Checks if Number is odd or even'''
	evenodd = number % 2	
	
	if number > 0:
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
			
		if standard10 > number >= standard1:
			return count
			programOn = False
			
		else:
			standard1 = standard1 * 10
			standard10 = standard10 * 10
				
		
	
	
def sum_of_less_digits(digit):
	'''Gets the sum of the digits less than the original digit'''
	sum = 0
	for item in range(digit):
		sum += item
	
	return sum

def sum_of_digits(number):
	'''Adds the digits in any number'''
	sum = 0
	
	while number > 0:
		singleDigit = number % 10
		number = number - singleDigit
		sum = sum + singleDigit
		number = number / 10
		
	return sum

def factorial(number):
	'''Gets the factorial of a given number'''
	factorial = 1
	for item in range(1,number):
		factorial *= item
	
	return factorial

def factoring(number, factor):
	'''Tells whether or not a the chosen number is a factor of the other number'''
	if factor == 0:
		return False
		
	else:	
		remainder = number % factor
		
		if remainder > 0:
			return False
			
		else:
			return True

def prime(number):
	"""This function checks if the argument is prime"""
	count = 2 #start count at 2 because 1 is a factor of every number
	while count != number:
 		remainder = number % count 
 		
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
 			if number % count == 0:
 				factorTotal += count
 			count += 1
 			
	if factorTotal == number:
		return True
	else:
		return False

def sum_div(number):
	'''checks if the sum of the digits of a number is a factor of the original number'''
	total = sum_of_digits(number)
	remainder = number % total
	if remainder == 0:
		return True
	else:
		return False
	
	
 			