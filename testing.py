import random

answer=random.randint(1,10)
def guess_game(guess,answer):
	if 0<guess<11:
		if guess==answer:
			print('You are a genius!')
			return True
	else:
		print('hey bro, between 1 and 10, remember?')
		return False
		
if __name__ == '__main__':
	while True:
		try:
			guess=int(input('guess a number between 1 and 10'))
			if (guess_game(guess,answer)):
				break
		except ValueError:
			print('please enter a number')
			continue
