import requests

response = requests.post('https://playground.learnqa.ru/api/check_type', data= {"param1":"value1"})
print(response.status_code)



response = requests.post('https://playground.learnqa.ru/api/get_500')
print(response.status_code)
print(response.text)


response = requests.post('https://playground.learnqa.ru/api/something')
print(response.status_code)
print(response.text)


response = requests.post('https://playground.learnqa.ru/api/get_301', allow_redirects=False)
print(response.status_code)
print(response.text)


response = requests.post('https://playground.learnqa.ru/api/get_301', allow_redirects=True)
first_re= response.history[0]
second_re= response

print(first_re.url)
print(second_re.url)