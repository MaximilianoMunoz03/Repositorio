import requests
import json


Earth_imagery = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"
data2 = requests.get(Earth_imagery)
tt2 = json.loads(data2.text)
print (tt2)
