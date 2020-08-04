from functools import reduce
my_list=[1,2,3]
your_list=[10,20,30]
their_list=[5,4,3]
def check_odd(item):
	return item % 2 != 0

def accumulator(acc,item):
	print(acc,item)
	return acc+item

print(list(zip(my_list,your_list)))
print(list(zip(my_list,your_list,their_list)))
print(list(filter(check_odd,my_list)))
print(my_list)
print(reduce(accumulator,my_list,9)) #function_name,variable,initial_value