from unittest import result
import requests

url = "https://discord.com/api/webhooks/101202105575959XXXX/DdAqi-bbLpuE3uhIg3taXUbLveRX9LU_XXXXXXXXXXXXXXXXXX"

data = {
    "content" : "fais chier",
    "username" : "Guy Boyz"
}
result = requests.post(url,json=data)
print("Payload Delivery, code {}".format(result.status_code))