import pytest

from data import product_data, user_data, login_data
from services import product_requests, login_requests, user_requests

data_product = product_data.DataProduct
product_request = product_requests.ProductRequest
login_request = login_requests.LoginRequests
user_request = user_requests.UserRequests
user_data = user_data.DataUser
login_data = login_data.DataLogin


class TestProduct:

    @pytest.fixture(autouse=True)
    def create_user_for_test(self):
        user_payload = user_data.new_user_payload()
        post_response = user_request.create_user(user_payload)
        assert post_response.status_code == 201
        login_payload = login_data.new_login_payload(user_payload["email"], user_payload["password"])
        login_response = login_request.post_login(login_payload)
        login_json = login_response.json()
        print(login_json)
        assert login_response.status_code == 200
        # global_pytest variables initialized
        pytest.token = login_json["authorization"]

    def test_get_products(self):
        product_response = product_request.get_products(None)
        assert product_response.status_code == 200

    def test_create_product(self):
        payload = data_product.new_product_payload()
        print(payload)
        product_response = product_request.create_product(payload, pytest.token)
        assert product_response.status_code == 201
        product_json = product_response.json()
        print(product_json)

    def test_get_product_by_id(self):
        pass

    def test_delete_product(self):
        pass

    def test_update_product(self):
        pass
