import requests
import json

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'


with open('patient.json', 'r') as f_in:   
    patient = json.load(f_in)

result = requests.post(url, json=patient).json()
print(result)