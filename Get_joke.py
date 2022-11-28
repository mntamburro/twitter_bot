


import json
from collections import namedtuple
from json import JSONEncoder
from urllib.request import urlopen

url= "http://official-joke-api.appspot.com/random_joke"
data = urlopen(url)
#print(r.getcode())
jsonData = json.loads(data.read())

print(jsonData['setup'])
print(jsonData['punchline'])