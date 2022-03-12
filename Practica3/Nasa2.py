import requests
import json


start_date= "https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY"
data = requests.get(start_date)
tt = json.loads(data.text)
print(tt)
