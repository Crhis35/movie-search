import json
import requests
import urllib3
urllib3.disable_warnings()

query = {
    'query': {
        'match': {
            'title': 'jumanji'
        }
    }
}
query = json.dumps(query)
print(query)
endpoint = 'https://localhost:9200'
username= 'admin'
password= 'admin'
url = endpoint + '/movies/_search'
r = requests.get(url, 
                 auth=(username, password),
                 data=query,
                 verify=False,
                 headers={'Content-type': 'application/json'})
print(r.json())