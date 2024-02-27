import pytest
import requests

class TestUserAuth:
    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        assert "auth_sid" in response1.cookies, "нет куки"
        assert "x-csrf-token" in response1.headers, "нет токена"
        assert "user_id" in response1.json(), "нет id пользователя"

        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x-csrf-token")
        self.user_id_1 = response1.json()["user_id"]

    def test_auth_user(self):

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
             headers = {"x-csrf-token": self.token},
             cookies = {"auth_sid": self.auth_sid}
        )

        assert "user_id" in response2.json(), "no user id"
        user_id_2 = response2.json()["user_id"]

        assert self.user_id_1 == user_id_2, "no user id =="

