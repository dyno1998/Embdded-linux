import requests
import json

url = "https://www.boredapi.com/api/activity"


response = requests.get(url)

 
if response.status_code == 200:
  
    data_json = response.json()

    # print the JSON response
    print(data_json['activity'])
else:
    print("Error:", response.status_code)
