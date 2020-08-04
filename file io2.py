
try:
	with  open('unknown.txt',mode='r+') as myf:
		texty=myf.write('Hey bitch ! It\'s me!')
		print(myf.readlines())

	with  open('unknown.txt',mode='a') as myf:
		text=myf.write(';)')
	
	with  open('unknown.txt',mode='r') as myf:
		print(myf.readlines())

except FileNotFoundError as Error:
	print('File is not present')
	raise Error	
except IOError as err:
	print('IO Error')
	raise err