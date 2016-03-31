
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

