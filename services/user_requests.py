import requests

import setup.setup

ENDPOINT = setup.setup.SetupClass.base_url()


class UserRequests:

    def create_user(self):
        return requests.post(ENDPOINT + '/usuarios', json=self)

    def update_user(self, _id):
        return requests.put(ENDPOINT + f'/usuarios/{_id}', json=self)

    def get_user(self):
        return requests.get(ENDPOINT + '/usuarios')

    def delete_user(self):
        return requests.delete(ENDPOINT + f'/usuarios/{self}')

    def get_user_by_id(self):
        return requests.get(ENDPOINT + f'/usuarios/{self}')
