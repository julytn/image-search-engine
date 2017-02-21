from clarifai.rest import ClarifaiApp
import json

app = ClarifaiApp('8g-Q8QAGb9ShZ0wknjem0JxNd4oE1Iqi0d-6xPuF', '96BW52C5aZcNdkNNRihOOhSzJzUQxMpBAG0BiMFA')

def search(query, page=1, per_page=10):
	result = app.inputs.search_by_predicted_concepts(concept=query, page=page, per_page=per_page)
	return [img.url for img in result]