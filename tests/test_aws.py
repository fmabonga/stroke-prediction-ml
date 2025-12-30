import requests
import json

url = 'https://damkfyq7ji.execute-api.us-east-1.amazonaws.com/test/predict'


with open('patient.json', 'r') as f_in:   
    patient = json.load(f_in)

result = requests.post(url, json=patient).json()
print(result)