import requests
import json
import webbrowser

def nasapic():

    params = {"api_key": "DEMO_KEY", "hd": True, "count" : 1}    
    f = r"https://api.nasa.gov/planetary/apod?"
    data = requests.get(f, params = params)
    tt = json.loads(data.text)
    
    print(tt[0]["title"])
    webbrowser.open(tt[0]["url"])
nasapic()
