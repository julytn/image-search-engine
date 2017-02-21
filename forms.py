from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, validators, ValidationError

class SearchForm(FlaskForm):
	query = TextField("Search for images in images.txt", [validators.Required()])
	submit = SubmitField("Send")