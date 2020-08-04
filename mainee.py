from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
my_pet=[i.upper() for i in my_pets ]
print(my_pet)

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
ny=list(zip(my_strings,my_numbers))
print(ny)
ny.sort(key= lambda i: i[1])
print(ny)

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
my_Sc=list(filter(lambda item: item/100>0.5 ,scores))
print(my_Sc)
#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
print(reduce(lambda a,b:a+b,(my_numbers+scores)))