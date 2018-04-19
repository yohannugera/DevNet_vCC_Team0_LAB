#Libraries and Functions always come in handy to developers by allowing reusability of existing code. There are certain well known inherent libraries that you have access to after installing python. By using these libraries and functions in them, write a program (in Python 3) to guess a randomly generated number between 1 and 10. 
#For Example: 
#
#Guess the number: 4
#Wrong, try again! 
#
#Guess the number: 8
#Correct! 
#
#Hint: Figure out which library the “randint” function belongs to. 

import random

x = random.randint(1,10)
while(1):
	y = input("Guess the number: ")
	if (x == eval(y)):
		print("Correct!")
		print()
		exit()
	else:
		print("Wrong, try again!")
		print()