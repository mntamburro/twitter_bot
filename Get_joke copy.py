
import json
from collections import namedtuple
from json import JSONEncoder
from urllib.request import urlopen

url= "http://official-joke-api.appspot.com/random_joke"
data = urlopen(url)
#print(r.getcode())
jsonData = json.loads(data.read())


class Joke:
    def __init__(self, setup, punchline) -> None:
        self.setup, self.punchline = setup, punchline

class RandomJoke(JSONEncoder):
    def default(self, o):
        return o.__dict__

def customjoke(jsonData):
    return namedtuple('X',jsonData.keys())(*jsonData.values())




print (jsonData)



Jokestr = json.loads(jsonData, object_hook=lambda d: namedtuple('X', d.keys(),*d.values()))

print(Jokestr.setup, Jokestr.punchline)
