import requests
import json


Earth_imagery = "https://api.nasa.gov/planetary/earth/imagery?lon=100.75&lat=1.5&date=2014-02-01&api_key=DEMO_KEY"
data2 = requests.get(Earth_imagery)
tt2 = json.loads(data2.text)
print (tt2)
