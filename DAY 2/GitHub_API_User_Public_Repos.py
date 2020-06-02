# Get a list of all repositories from the user list generated from the last API Call to GitHub's REST API
import requests
import json
from pprint import pprint
url = f"https://api.github.com/users?"
data = requests.get(url).json()
user_list = []
for i in data:
	user_list.append(i['login'])
for i in user_list:
	url = "https://api.github.com/users/{}/repos".format(i)
	data = requests.get(url).json()
	with open("User_Repos.json", "a") as outfile: 
		json.dump(data,outfile)
