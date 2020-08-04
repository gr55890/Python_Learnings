def hello():
	print('meow')

greet=hello
print(greet())
del hello
#hello()
print(greet())

#Higher Order Function
def greet(func):
	func()

def greet2():
	def func():
		return 5
	return func

#Example : map, reduce, filter
#Decorators
def my_decorator(func):
	def wrap_func():
		print("****************")
		func()
		print("****************")
	return wrap_func

@my_decorator
def hello():
	print('hellllooooo')

@my_decorator
def bye():
	print('bye bye')

hello()
bye()

my_decorator(hello)()
