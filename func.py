#map, filter, zip, reduce

wizard={
	'name':'Merlin',
	'power':50
}
#new_list=[]
def multiply_by2(li):
	new_list = []
	for item in li:
		new_list.append(item*2)
	return print(new_list)

#new_list=''
multiply_by2([1,2,3])
def multiply_by(item):
	return item*2

print(list(map(multiply_by,[1,2,3])))