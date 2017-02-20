from flask import Flask, render_template, request, flash
from forms import SearchForm
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/', methods = ['GET', 'POST'])
def search():
	form = SearchForm()

	if request.method == 'POST':
		if not form.validate():
			flash('All fields are required.')
			return render_template('search.html', form = form)
		else:
			return render_template('success.html')
	elif request.method == 'GET':
		return render_template('search.html', form = form)

if __name__ == '__main__':
	app.run(debug = True)