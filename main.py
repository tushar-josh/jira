import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://jtgteam.atlassian.net/rest/api/3/search"

auth = HTTPBasicAuth("tushar.gupta@joshtechnologygroup.com", "cRgJNELcqadieXu1p31j7A37")

headers = {
   "Accept": "application/json",
    "Content-Type" : "application/json"
}

query = {
   'jql': 'project = TEST1'
}

payload = json.dumps(
   {
      "transition":{
         "id" : "21"
      }
   }
)

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query,
   auth=auth
)

data = response.json()
issues = data["issues"]
for issue in issues:
    print(issue["key"])
