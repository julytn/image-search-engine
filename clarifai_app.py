from clarifai import rest
from clarifai.rest import ClarifaiApp, Image as ClImage
import json

batch_size = 127 # 128 gives 500 error 
app = ClarifaiApp()

# get the general-v1.3 model
model = app.models.get("aaa03c23b3724a16a56b629203edc62c")

# read in images
images = []
i = 1
f = open('images.txt', 'r')
for line in f:
	images.append(ClImage(url=line.rstrip(), image_id=str(i)))
	i += 1

d = {}
for i in range(8):
	# tag images
	prediction = model.predict(images[i * batch_size : (i + 1) * batch_size])
	d[i] = prediction

	# before search, first need to upload images
	app.inputs.bulk_create_images(images[i * batch_size : (i + 1) * batch_size])



# search by predicted concept
app.inputs.search_by_predicted_concepts(concept='dog')