import requests
import json

response = requests.get("http://universities.hipolabs.com/search?name=latvia")#, params={"alpha_two_code":"LV"}) Pirmais uzdevums

a = (json.dumps(response.json(), indent=4))
response_json = json.loads(a)


a = (sorted(response_json, key=lambda k: k['name'])) #Otrais uzdevums
print(a)
print(a["domain"]['name']) #tresais uzdevums





#print(response.status_code)
#print(response)
#print(response.headers)
#obj = json.loads(response.text)
#json_formatted_str = json.dumps(obj)
#print(json_formatted_str)
#print(response.json())
#print(json.dumps(response.json(), sort_keys=True))
#b = sorted(json_formatted_str, key=lambda k: k['name'])
#data = json.loads(json_formatted_str)
#data = json.dumps(data)
#c = json.dumps(data)
#print(json_formatted_str["name"])
#indent=4
