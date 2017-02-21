from clarifai.rest import ClarifaiApp, Image as ClImage

batch_size = 128
app = ClarifaiApp('8g-Q8QAGb9ShZ0wknjem0JxNd4oE1Iqi0d-6xPuF', '96BW52C5aZcNdkNNRihOOhSzJzUQxMpBAG0BiMFA')

# get the general-v1.3 model
model = app.models.get("aaa03c23b3724a16a56b629203edc62c")

# process 1000 images
images = []
results = {}
batch_number = 1
f = open('images.txt', 'r')
for line in f:
	if len(images) < batch_size:
		images.append(ClImage(url=line.rstrip()))
	else:
		# tag 128 images
		results[batch_number] = model.predict(images)
		
		# before search, first need to upload images
		app.inputs.bulk_create_images(images)

		# ready for next batch
		images = [ClImage(url=line.rstrip())]
		batch_number += 1

# last batch
results[batch_number] = model.predict(images)
	