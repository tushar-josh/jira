import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://jtgteam.atlassian.net/rest/api/3/issue/TEST1-1/transitions"

auth = HTTPBasicAuth("tushar.gupta@joshtechnologygroup.com", "cRgJNELcqadieXu1p31j7A37")

headers = {
   "Accept": "application/json",
    "Content-Type" : "application/json"
}

payload = json.dumps(
   {
      "transition":{
         "id" : "21"
      }
   }
)

response = requests.request(
   "POST",
   url,
   headers=headers,
   data=payload,
   auth=auth
)
print(response.status_code)