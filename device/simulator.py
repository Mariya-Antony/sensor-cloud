import requests

url = "http://127.0.0.1:8000/reading"

dict1 = {'device_id': 'pi-1', 'temperature_c': 23.45}

response = requests.post(url, json = dict1)
print(response.json())

