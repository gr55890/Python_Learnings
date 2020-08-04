#OOP
class PlayerCharacter:
	membership=True
	def __init__(self,name,age):
		if(self.membership):	
			self._name=name  #private
			self._age=age

	def run(self):
		print('run')
	def speak(self):
		print(f'My name is {self._name} and age is {self._age}.')


player1=PlayerCharacter('Andrei',100)	
player1.speak()
player1.name='?io'
player1.speak='BOOOOO'
print(player1.speak)