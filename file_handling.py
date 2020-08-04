#Write a script that handles opening a non-existing file, 'unknown_file.txt', and prints the message File not found. to the user.

'''
file = open('unknown.txt','w')
file.write('Meow')
file.close()
'''

#------------Odd Even Wala Problem-----------#
import itertools
def even_or_odd(n):
    if n%2==0:
        return 'even'
    else:
        return 'odd'

n=[10,14,16,22,9,3,37]
l=[even_or_odd(m) for m in n]
ita=list(zip(l,n))
print(ita) 
an_iterator = itertools.groupby(ita, lambda x : x) 
  
for key, group in an_iterator: 
    key_and_group = {key : list(group)} 
    print(key_and_group) 
