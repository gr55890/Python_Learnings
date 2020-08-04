from collections import Counter,defaultdict,OrderedDict

li=[1,2,3,4,5,6,7,7]
sentence='blah blah blah thinking about python'
print(Counter(li))
print(Counter(sentence))

dictionary=defaultdict(int,{'a':1,'b':2})
print(dictionary['c'])
#provides default values for unknown variables which is eqivalent to --
print(int())

dictionary=defaultdict(lambda: 'doesn\'t exist',{'a':1,'b':2})
print(dictionary['c'])

d=OrderedDict()
d['a']=1
d['b']=2

d2=OrderedDict()
d2['a']=1
d2['b']=2

print(d2==d)

f={'c':100}
f['a']=1
f['b']=2

f2={'c':100}
f2['b']=2
f2['a']=1

print(f2==f)

