# Get list of GitHub repos that have their main language as Java, and have their topic as REST
import requests
import json
from pprint import pprint
url = f"https://api.github.com/search/repositories?q=language:Java&topic=REST"
data = requests.get(url).json()
with open("Java_Rest.json", "a") as outfile: 
	json.dump(data,outfile)
