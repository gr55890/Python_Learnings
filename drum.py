class User():
	def __init__(self,email):
		self.email=email

	def sign_in(self):
		print('Logged In')

class Wizard(User):
	def __init__(self,name,power,email):
		User.__init__(self,email)  #or super().__init__(email)
		self.name=name
		self.power=power


	def attack(self):
		print(f'attacking with power of {self.power}')

wizard1=Wizard('Merlin',50,'merlin@gmail.com')
print(wizard1.email)
print(dir(wizard1))
print(issubclass(list,list))