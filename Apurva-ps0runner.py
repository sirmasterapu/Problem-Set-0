import Apurvaps0

runner = raw_input("What program would you like?\n0. Even or Odd\n1.Number of Digits\n2.Sum of lesser digits\n3.Sum of digits\nEnter the number: ")


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