from functools import reduce
#lambda expressions
lambda param: action(param)
my_list=[1,2,3]
print(list(map(lambda item:item*2, my_list)))
print(list(filter(lambda item: item%2!=0, my_list)))
print(reduce(lambda acc,item:acc+item,my_list))
arizhanan=[5,4,3]
print(list(map(lambda item:item**2,arizhanan)))
salivanan=[(0,2),(4,3),(9,9),(10,-1)]
salivanan.sort(key=lambda x: x[1])
print(salivanan)