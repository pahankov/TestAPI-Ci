import requests

def test1_get_basic():
    r = requests.get("https://postman-echo.com/get")
    assert r.status_code == 200, f"Статус: {r.status_code}, Ответ: {r.text}"
    data = r.json()
    assert "args" in data and "headers" in data and "url" in data
    print("✅ Тест базовый пройден")

def test2_get_with_query_params():
    params = {"name": "John", "city": "Moscow", "age": "30"}
    r = requests.get("https://postman-echo.com/get", params=params)
    assert r.status_code == 200, f"Статус: {r.status_code}, Ответ: {r.text}"
    data = r.json()
    assert data["args"]["name"] == "John"
    assert data["args"]["city"] == "Peterburg"
    print("✅ Тест GET с параметрами URL пройден")

def test3_get_with_headers():
    headers = {"User-Agent": "My-Test-Bot", "X-Request-ID": "12345"}
    r = requests.get("https://postman-echo.com/get", headers=headers)
    assert r.status_code == 200, f"Статус: {r.status_code}, Ответ: {r.text}"
    data = r.json()
    assert "user-agent" in data["headers"]
    assert data["headers"]["user-agent"] == "My-Test-Bot"
    print("✅ Тест GET с кастомными заголовками пройден")

def test4_post_form_data():
    form_data = {"username": "test_user", "password": "secret123"}
    r = requests.post("https://postman-echo.com/post", data=form_data)
    assert r.status_code == 200, f"Статус: {r.status_code}, Ответ: {r.text}"
    data = r.json()
    assert data["form"]["username"] == "test_user"
    assert data["form"]["password"] == "secret123"
    print("✅ Тест POST с form-data пройден")

def test5_post_json_data():
    json_data = {"message": "Hello", "count": 42, "active": True}
    r = requests.post("https://postman-echo.com/post", json=json_data)
    assert r.status_code == 200, f"Статус: {r.status_code}, Ответ: {r.text}"
    data = r.json()
    assert data["json"]["message"] == "Hello"
    assert data["json"]["count"] == 42
    assert data["json"]["active"] == True
    print("✅ Тест POST с JSON телом пройден")


test1_get_basic()
test2_get_with_query_params()
test3_get_with_headers()
test4_post_form_data()
test5_post_json_data()

