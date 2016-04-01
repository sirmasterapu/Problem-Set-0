import Apurvaps0

runner = raw_input("What program would you like?\n0. Even or Odd\n1.Number of Digits\n2.Sum of lesser digits\n3.Sum of digits\n4. The factorial of a number\n5. factoring of a number\n6. Tests whether a number is prime or not\n7. Tests for a perfect number\n8. Tests is the sum of a number is also a factor\nEnter the number: ")


#The Even or Odd function
if runner == "0":
	#Test Case 1: Odd Number
	print("Is 5 even? {} ".format(Apurvaps0.odd_or_even(5)))
	#Test Case 2: Even Number
	print("Is 2 even? {} ".format(Apurvaps0.odd_or_even(2)))
	#Test Case 3: 0
	print("Is 0 even? {} ".format(Apurvaps0.odd_or_even(0)))

#The Number of digits function
if runner == '1':
 	#Test Case 1: 2 digit number
 	print(" 11 contains {} digits. ".format(Apurvaps0.length(11)))
 	#Test Case 2: 10 digit number
 	print("1111111111 contains {} digits.".format(Apurvaps0.length(1111111111)))
 	#Test Case 3: 1 digit number
 	print("0 contains {} digits.".format(Apurvaps0.length(0)))
 

#This is the Sum of the lesser digits function
if runner == '2':
#Test case 1: testing that 1 outputs 0
	print ("The sum of the digits before 1 is {}.".format(Apurvaps0.sum_of_less_digits(1)))
#Test case 2: regular testing
	print ("The sum of the digits before 3 is {}.".format(Apurvaps0.sum_of_less_digits(3)))
#Test case 3: always test 0 
	print ("The sum of the digits before 0 is {}.".format(Apurvaps0.sum_of_less_digits(0)))

#This is the digit addition of any given number function
if runner == '3':
#Test case 1: testing a random number
	print("The sum of the digits of 1234 is {}".format(Apurvaps0.sum_of_digits(1234)))
#Test case 2: testing 0 because why not
	print("The sum of the digits of 0 is {}".format(Apurvaps0.sum_of_digits(0)))
	
if runner == '4':
#Test case 1: testing a given number
	print("The factorial of 7 is {}".format(Apurvaps0.factorial(7)))
#Test case 2: testing 1
	print("The factorial of 1 is {}".format(Apurvaps0.factorial(1)))
#Test case 3: testing 0
	print("The factorial of 0 is {}".format(Apurvaps0.factorial(0)))

if runner == '5':
#Test case 1: testing a given number and factor
	print("Is 2 a factor of 4? {}".format(Apurvaps0.factoring(4, 2)))
#Test case 2: testing a given number and a non factor
	print("Is 3 a factor of 4? {}".format(Apurvaps0.factoring(4, 3)))
#Test case 3: testing a given number and 0
	print("Is 0 a factor of 4? {}".format(Apurvaps0.factoring(4, 0)))
#Test case 4: The factors of 0
	print("Is 4 a factor of 0? {}".format(Apurvaps0.factoring(0, 4)))
	
if runner == '6':
#Test case 1: testing a prime number
	print("Is 23 prime? {}".format(Apurvaps0.prime(23)))
#Test case 2: testing a non prime number
	print("Is 15 prime? {}".format(Apurvaps0.prime(15)))
#Test case 3: testing border 2
	print("Is 2 prime? {}".format(Apurvaps0.prime(2)))

if runner == '7':
#Test case 1: perfect number
	print("Is 6 a perfect number? {}".format(Apurvaps0.perfect(6)))
#Test case 2: non perfect number
	print("Is 10 a perfect number? {}".format(Apurvaps0.perfect(10)))

if runner == '8':
#Test case 1: factorable number
	print("Is the sum of the digits 12 a factor of 12? {}".format(Apurvaps0.sum_div(12)))
#Test case 2: non factorable number
	print("Is the sum of the digits 15 a factor of 15? {}".format(Apurvaps0.sum_div(15)))

