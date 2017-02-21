from clarifai.rest import ClarifaiApp
import json

app = ClarifaiApp()

def search(query, page=1, per_page=10):
	result = app.inputs.search_by_predicted_concepts(concept=query, page=page, per_page=per_page)
	return [img.url for img in result]