import pytest
# данные
NAME = "Филипп"
CITY = "Москва"
AGE_STR = "30"
AGE_NUMBER = 47
PASSWORD = "password12345"
MESSAGE = "Привет"
USER_AGENT = "Test-Agent"
REQUEST_ID = "12345"

# ссылка для API запросов
@pytest.fixture
def base_url():
    return "https://postman-echo.com"

# HTTP ответ статус 200
@pytest.fixture
def verification_status_200():
    def take_status(response):
        assert response.status_code == 200
        return response.json()
    return take_status

# GET данные
@pytest.fixture
def get_headers():
    return {
        "User-Agent": USER_AGENT,
        "X-Request-ID": REQUEST_ID
    }

# form-data запросы
@pytest.fixture
def form_data():
    return {
        "username": NAME,
        "password": PASSWORD
    }

# JSON запросы
@pytest.fixture
def json_data():
    return {
        "message": MESSAGE,
        "age": AGE_NUMBER,
        "online": True
    }

# GET запросы
@pytest.fixture
def query_params():
    return {
        "name": NAME,
        "city": CITY,
        "age": AGE_STR
    }

