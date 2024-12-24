import pytest
import yaml
import requests

#Загрузка конфигурации
with open("config.yaml") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def login():
    res1 = requests.post(
        data["address"] + "gateway/login",
        data={"username": data["username"], "password": data["password"]}
    )
    print(res1.content)
    return res1.json()["token"]

@pytest.fixture()
def testtext1():
    return "test"

@pytest.fixture()
def create_post(login):
    def create_post(title, description, content):
        header = {"X-Aut-Token": login}
        payload = {
            "title": title,
            "description": description,
            "content": content
        }
        res = requests.post(data["address"] + "api/posts", headers=header, json=payload)
        print(res.content)
        assert res.status_code == 200
        return payload  # Возврат данных созданного поста для проверки
    return create_post
