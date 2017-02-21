import json

j = '{"status": {"code": 10000,"description": "Ok"},"hits": [{"score": 0.98155165,"input": {"id": "f96ca3bbf02041c59addcc13e3468b7d","created_at": "2016-11-22T17:06:02Z","data": {"image": {"url": "https://samples.clarifai.com/wedding.jpg"}},"status": {"code": 30000,"description": "Download complete"}}}]}'


o = json.loads(j)
print o

print o['hits'][0]['input']['data']['image']['url']
print o['hits'][0]['score']