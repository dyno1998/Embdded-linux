import requests
import json

url = "https://api.ipify.org/?format=json"

response = requests.get(url)
 
if response.status_code == 200:
  
    data_json = response.json()

    # print the JSON response
    print(data_json['ip'])
else:
    print("Error:", response.status_code)
