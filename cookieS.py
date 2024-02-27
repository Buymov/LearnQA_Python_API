import requests

payload = {"login":"secret_login", "password":"secret_pass"}
response = requests.post('https://playground.learnqa.ru/api/get_auth_cookie', data=payload)

print(response.text)
print(response.status_code)
print(dict(response.cookies))


payload = {"login":"secret_login", "password":"secret_pass2"}
response = requests.post('https://playground.learnqa.ru/api/get_auth_cookie', data=payload)

print(response.text)
print(response.status_code)
print(dict(response.cookies))