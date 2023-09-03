import pytest

from services import user_requests
from services import login_requests
from data import user_data
from data import login_data

login_request = login_requests.LoginRequests
user_request = user_requests.UserRequests
user_data = user_data.DataUser
login_data = login_data.DataLogin


class TestLogin:

    @pytest.fixture(autouse=True)
    def create_user_for_test(self):
        user_payload = user_data.new_user_payload()
        post_response = user_request.create_user(user_payload)
        assert post_response.status_code == 201
        # global_pytest variables initialized
        pytest.email = user_payload["email"]
        pytest.password = user_payload["password"]

    def test_login_success(self):
        login_payload = login_data.new_login_payload(pytest.email, pytest.password)
        login_response = login_request.post_login(login_payload)
        login_json = login_response.json()
        assert login_response.status_code == 200
        assert login_json["message"] == "Login realizado com sucesso"
        print(login_json)

    def test_login_fail(self):
        login_payload = login_data.new_login_payload(pytest.email, "wrong_password")
        login_response = login_request.post_login(login_payload)
        login_json = login_response.json()
        assert login_response.status_code == 401
        assert login_json["message"] == "Email e/ou senha inválidos"
        print(login_json)

    def test_login_without_email(self):
        login_payload = login_data.new_login_payload("", pytest.password)
        login_response = login_request.post_login(login_payload)
        login_json = login_response.json()
        assert login_response.status_code == 400
        assert login_json["email"] == "email não pode ficar em branco"
        print(login_json)
