from flask import Flask,render_template
app=Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
	return 'Hello,world!'

@app.route('/blog')
def user():
	return 'This is my first blog!'

@app.route('/blog/2020/dogs')
def user2():
	return 'There are a lotta dogs everywhere !'

@app.route('/blog/2020/cats')
def usr():
	return render_template('m.html')