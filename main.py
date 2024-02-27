import requests
from json.decoder import JSONDecodeError

#response = requests.get('https://playground.learnqa.ru/api/get_text')
#print(response.text)

response = requests.get('https://playground.learnqa.ru/api/get_text')
print(response.text)

try:
    parsed_text = response.json()
    print(parsed_text["answer"])
except JSONDecodeError:
    print("Respons is not Json format")


