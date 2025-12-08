'''
Created on 30-Nov-2025

@author: haripriya

'''
import requests

response = requests.get("https://api.restful-api.dev/objects/5")
print("response:",response)
status_code = response.status_code
print("response.status_code:", response.status_code)
response_body = response.json()
print("response.json():", response_body)
object_id = response_body["id"]
print("object_id:", object_id)
price = response_body["data"]["price"]
print("price:", price)
