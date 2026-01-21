import requests

# GET запрос
def test1_get_basic(base_url, verification_status_200):
    r = requests.get(f"{base_url}/get")
    data = verification_status_200(r)
    assert "args" in data and "headers" in data and "url" in data

# GET с квери-параметрами
def test2_get_with_query_params(base_url, verification_status_200, query_params):
    r = requests.get(f"{base_url}/get", params=query_params)
    data = verification_status_200(r)
    assert data["args"] == query_params

# GET с заголовками
def test3_get_with_headers(base_url, verification_status_200, get_headers):
    r = requests.get(f"{base_url}/get", headers=get_headers)
    data = verification_status_200(r)
    assert data["headers"]["user-agent"] == get_headers["User-Agent"]
# Ломаем тест
    # assert data["headers"]["x-request-id"] == get_headers["X-Request-ID"]

# POST с form-data
def test4_post_form_data(base_url, verification_status_200, form_data):
    r = requests.post(f"{base_url}/post", data=form_data)
    data = verification_status_200(r)
    assert data["form"] == form_data

# POST с JSON
def test5_post_json_data(base_url, verification_status_200, json_data):
    r = requests.post(f"{base_url}/post", json=json_data)
    data = verification_status_200(r)
    assert data["json"] == json_data





