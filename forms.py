from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms import validators, ValidationError

class SearchForm(Form):
	query = TextField("Search for image", [validators.Required("Please enter something.")])
	submit = SubmitField("Send")