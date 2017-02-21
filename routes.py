from flask import Flask, render_template, request, flash
from forms import SearchForm
import clarifai_search as cs

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
	form = SearchForm()

	if request.method == 'POST':
		if not form.validate():
			flash('Please enter a search.')
			return render_template('search.html', form=form)
		else:
			result = cs.search(form.query.data)
			if type(result) is list:
				return render_template('search.html', success=True, images=result, form=form)
			else:
				flash(result)
				return render_template('search.html', form=form)
	elif request.method == 'GET':
		return render_template('search.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)