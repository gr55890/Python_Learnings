#OOP
class PlayerCharacter:
	membership=True
	def __init__(self,name,age):
		if(self.membership):	
			self.name=name 
			self.age=age

	def shout(self):
		print(f'My name is {self.name}')

	@classmethod
	def adding_things(cls,num1,num2):
		return num1+num2
		#return cls('Teddy',num1+num2)

	@staticmethod
	def subtract_things(num1,num2): #cls not supported
		if num1>num2:
			return num1-num2
		else:
			return num2-num1

player1=PlayerCharacter('Tom',20)
print(player1.adding_things(10,4))
print(PlayerCharacter.adding_things(10,4))
player3=PlayerCharacter.adding_things(2,3)
print(player3)
player4=PlayerCharacter.subtract_things(8,18)
print(player4)
