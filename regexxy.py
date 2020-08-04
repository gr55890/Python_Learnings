import re
pattern=re.compile(r"([a-zA-Z]).([a])")
str1='search this inside this text!'
email=re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
str2='gr55890@gmail.com'

a=pattern.search(str1)
b=email.search(str2)
print(a.group())
print(b.group())
print(a)
print(b)

##################PASSWORD##########################################################
# At least 8 char
# contain any sort of letters, numbers, $%#@
# has to end with a number

password=re.compile(r"(^[a-zA-Z0-9$%#@]{8,}\d)")
str3='seCReti987@#3'
str4='Rtv89ujkl%@o1'
c=password.search(str3)
print(c.group())
print(c)
d=password.search(str4)
print(d.group())
print(d)

