class User(object):
	def __init__(self,email):
		self.email=email
		print('init complete')

	def sign_in(self):
		print('logged in')

class Wizard(User):
	def __init__(self,name,power):
		self.name=name
		self.power=power
	
	def attack(self):
		print(f'attacking with a power of {self.power}')

class Archer(User):
	def __init__(self,name,arrows):
		self.name=name
		self.arrows=arrows

	def check_Arrows(self):
		print(f'{self.arrows} remaining')

	def run(self):
		print('ran really fast')

class HybridBorg(Wizard,Archer):
	def __init__(self,name,power,arrows):
		Archer.__init__(self,name,arrows)
		Wizard.__init__(self,name,power)

wz1=Wizard('Borgie',50)
ar2=Archer('Alex',90)

hb1=HybridBorg('Rudranil',100,50)

print(hb1.run())
print(hb1.check_Arrows())
print(hb1.sign_in())
print(hb1.attack())