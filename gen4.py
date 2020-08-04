def fib(num):
	x,y=0,1
	for i in range(num):
		yield x
		temp=x
		x=y
		y=temp + y

for x in fib(21):
	print(x)

def fib2(num):
	x,y=0,1
	result=[]
	for i in range(num):
		result.append(x)
		temp=x
		x=y
		y=temp + y
	return result

print(fib2(100))
