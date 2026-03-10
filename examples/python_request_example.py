import requests

url = "https://filterdata.ru/api/v1/normalize"

payload = {
    "phone": "8 (999) 123-45-67",
    "name": "ивaнов иван",
    "email": "user@agmil.com"
}

response = requests.post(url, json=payload)

print(response.json())
