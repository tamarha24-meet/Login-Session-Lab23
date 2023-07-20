from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def home():
	if request.method == 'GET':
		return render_template('home.html')

	else:

		author = request.form['author'].lower()
		quote = request.form['quote']

		login_session['author'] = author
		login_session['quote'] = quote
		try:
			age = int(request.form['age'])
			login_session['age'] = age
			return render_template('thanks.html')
		except:
			return render_template('error.html')



@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():
	age = login_session['age']
	quote = login_session['quote']
	author = login_session['author']

	return render_template('display.html', age = age, author = author, quote = quote) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)