from random import randint
#import sys

#answer=randint(sys.argv[1],sys.argv[2])
answer=randint(1,10)
while True:
	try:
		guess=input('guess a number 1~10')
		if int(guess)>0 and int(guess)<11:
			if int(guess)==answer:
				print('You are a genius!')
				break
		else:
			print('Hey Bozo, enter a no. 0~10')
	except ValueError:
		print('Please enter a valid number')
		continue


		