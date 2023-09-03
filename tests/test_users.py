from services import user_requests
from data import user_data

request = user_requests.UserRequests
user_data = user_data.DataUser


class TestUsers:

    def test_get_users(self):
        get_response = request.get_user(None)
        assert get_response.status_code == 200

    def test_post_user(self):
        user_payload = user_data.new_user_payload()
        post_response = request.create_user(user_payload)
        user_json = post_response.json()
        print(user_json)
        assert post_response.status_code == 201

    def test_get_user_by_id(self):
        # create user
        user_payload = user_data.new_user_payload()
        post_response = request.create_user(user_payload)
        assert post_response.status_code == 201
        user_json = post_response.json()
        user_id = user_json["_id"]
        # get user created
        user_by_id_response = request.get_user_by_id(user_id)
        user_by_id_data = user_by_id_response.json()
        assert user_by_id_response.status_code == 200
        assert user_payload["nome"] == user_by_id_data["nome"]
        assert user_payload["email"] == user_by_id_data["email"]

    def test_delete_user(self):
        # create user
        user_payload = user_data.new_user_payload()
        post_response = request.create_user(user_payload)
        assert post_response.status_code == 201
        user_json = post_response.json()
        user_id = user_json["_id"]
        # delete user created
        user_delete_response = request.delete_user(user_id)
        user_delete_json = user_delete_response.json()
        assert user_delete_response.status_code == 200
        assert user_delete_json["message"] == "Registro excluído com sucesso"

    def test_put_user(self):
        # create user
        user_payload = user_data.new_user_payload()
        post_response = request.create_user(user_payload)
        assert post_response.status_code == 201
        user_json = post_response.json()
        user_id = user_json["_id"]
        # update user created
        new_user_payload = user_data.new_user_payload()
        update_user_response = request.update_user(new_user_payload, user_id)
        update_user_json = update_user_response.json()
        assert update_user_response.status_code == 200
        assert update_user_json["message"] == "Registro alterado com sucesso"
