#OOP
class PlayerCharacter:
	#Class Object attribute
	membership=True
	#Dunder Method / Constructor
	def __init__(self,name,age):
		if(self.membership):	#if(PlayerCharacter.membership):
			self.name=name #attributes
			self.age=age

	def shout(self):
		print(f'My name is {self.name}')
	def run(self):
		print('run')
		return 'done'

player1=PlayerCharacter('Rudranil',26)
player2=PlayerCharacter('Tom',44)
player2.attack=50
print(player1)
print(player2)
print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)
print(player1.run)
print(player2.run())
print(player2.attack)
help(PlayerCharacter)
help(list)
print(player2.shout())