import re

pattern=re.compile('search this inside of this test please!')
string='search this inside of this test please! Hey Rudra!'
print('search' in string)
a=(re.search('this',string))
print(a.span())
print(a.start())
print(a.end())
print(a.group())

m=pattern.search(string)
b=pattern.findall(string)
c=pattern.fullmatch(string)
d=pattern.match(string)
print(m)
print(b)
print(c)
print(d)