from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms import validators, ValidationError

class SearchForm(FlaskForm):
	query = TextField("Search for image", [validators.Required("Please enter something.")])
	submit = SubmitField("Send")