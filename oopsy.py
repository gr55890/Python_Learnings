class PlayerCharacter:
	#Class Object attribute
	membership=True
	#Dunder Method / Constructor
	def __init__(self,name='anonymous',age=18):
		if(age>18):	#if(PlayerCharacter.membership):
			self.name=name #attributes
			self.age=age

	def shout(self):
		print(f'My name is {self.name}')

player1=PlayerCharacter()
player2=PlayerCharacter('Mom',14)
player3=PlayerCharacter('Dick')
player4=PlayerCharacter('Harry',19)
print(player1)
print(player2.name)
print(player3.name)
print(player4.name)