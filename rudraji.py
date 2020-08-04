#list, set, dictionary comprehensions

my_list=[]
for char in 'hello':
	my_list.append(char)

print(my_list)
simple_dict={
	'a':1,
	'b':2
}

my_list1=[param for param in 'hello']
my_list2={num*2 for num in range(1,100)}
my_list3=[num**2 for num in range(1,100)]
my_list4=[num**2 for num in range(1,100) if num%2==0 ]
#my_list5=[num**2 for num,i in range(1,100) if count(num%i==0)==2 ]
my_dict={key:value**2 for key,value in simple_dict.items()}
my_dict2={num:num*2 for num in [1,2,3]}

print(my_list1)
print(my_list2)
print(my_list3)
print(my_list4)
#print(my_list5)
print(my_dict)
print(my_dict2)

####################################################################
some_list=['a','b','c','b','d','m','n','n']
duplicates={item for item in some_list if some_list.count(item)>1}
print(duplicates)