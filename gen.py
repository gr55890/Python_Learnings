#iterable (go through the loop): __iter__
#take an item --> do something --> proceed to next one
#generators are iterable (they iterate over something) ex- range
#iterables are not always generators ex- list

#################################
#here values are not stored in memory

print(range(100))
print(list(range(100)))

def generator_function(num):
	for i in range(num):
		yield i*2

#for item in generator_function(1000):
#	print(item)

g=generator_function(100)
print(next(g))
print(next(g))
print(next(g))

#################################
#here values are stored in memory

def make_list(num):
	result=[]
	for i in range(num):
		result.append(i*2)
	return result

my_list=make_list(100)
print(my_list)