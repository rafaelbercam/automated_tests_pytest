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
        assert login_response.status_code == 200
        # global_pytest variables initialized
        pytest.token = login_json["authorization"]

    def test_get_products(self):
        product_response = product_request.get_products(None)
        product_response_json = product_response.json()
        assert product_response.status_code == 200
        print(product_response_json)

    def test_create_product(self):
        payload = data_product.new_product_payload()
        product_response = product_request.create_product(payload, pytest.token)
        assert product_response.status_code == 201
        product_json = product_response.json()
        assert product_json["message"] == "Cadastro realizado com sucesso"
        print(product_json)

    def test_get_product_by_id(self):
        # create product
        payload = data_product.new_product_payload()
        product_response = product_request.create_product(payload, pytest.token)
        assert product_response.status_code == 201
        product_json = product_response.json()
        id_product = product_json["_id"]
        # get product by id
        get_by_id_response = product_request.get_product_by_id(id_product)
        assert get_by_id_response.status_code == 200
        get_by_id_response_json = get_by_id_response.json()
        assert get_by_id_response_json["nome"] == payload["nome"]
        assert get_by_id_response_json["preco"] == payload["preco"]
        assert get_by_id_response_json["descricao"] == payload["descricao"]
        print(get_by_id_response_json)

    def test_delete_product(self):
        # create product
        payload = data_product.new_product_payload()
        product_response = product_request.create_product(payload, pytest.token)
        assert product_response.status_code == 201
        product_json = product_response.json()
        id_product = product_json["_id"]
        # delete product
        delete_response = product_request.delete_product(id_product, pytest.token)
        assert delete_response.status_code == 200
        delete_response_json = delete_response.json()
        assert delete_response_json["message"] == "Registro excluído com sucesso"
        print(delete_response_json)

    def test_update_product(self):
        # create product
        payload = data_product.new_product_payload()
        product_response = product_request.create_product(payload, pytest.token)
        assert product_response.status_code == 201
        product_json = product_response.json()
        id_product = product_json["_id"]
        # updated product
        new_payload_product = data_product.new_product_payload()
        product_update_response = product_request.update_product(new_payload_product, id_product, pytest.token)
        assert product_update_response.status_code == 200
        product_update_response_json = product_update_response.json()
        assert product_update_response_json["message"] == "Registro alterado com sucesso"
        print(product_update_response_json)
