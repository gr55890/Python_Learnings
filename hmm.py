import unittest
import testing

class Testy(unittest.TestCase):
	def testing_stuff(self):
		answer=6
		guess =6
		result=testing.guess_game(answer,guess)
		self.assertEqual(result,True)
	def testing_stuff2(self):
		answer=5
		guess =8
		result=testing.guess_game(answer,guess)
		self.assertFalse(result)
	def testing_stuff3(self):
		answer=5
		guess =11
		result=testing.guess_game(answer,guess)
		self.assertFalse(result)

	def testing_stuff4(self):
		answer=5
		guess ='8'
		result=testing.guess_game(answer,guess)
		self.assertFalse(result)


if __name__ == '__main__':
	unittest.main()