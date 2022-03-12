import requests
import json


Earth_imagery = "https://api.nasa.gov/techport/api/projects?api_key=DEMO_KEY"
data2 = requests.get(Earth_imagery)
tt2 = json.loads(data2.text)
print (tt2)
