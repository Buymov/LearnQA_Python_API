import requests

class TestUserAuth:
    def test_auth_user(self):
        data = {
            'email':'vinkotov@example.com',
            'password':'1234'
        }

        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        assert "auth_sid" in response1.cookies, "нет куки"
        assert "x-csrf-token" in response1.headers, "нет токена"
        assert "user_id" in response1.json(), "нет id пользователя"

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id_1 = response1.json()["user_id"]

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
             headers = {"x-csrf-token":token},
             cookies = {"auth_sid":auth_sid}
        )

        assert "user_id" in response2.json(), "no user id"
        user_id_2 = response2.json()["user_id"]

        assert user_id_1 == user_id_2, "no user id =="

