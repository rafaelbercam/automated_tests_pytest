import requests

import setup.setup

ENDPOINT = setup.setup.SetupClass.base_url()


class ProductRequest:

    def create_product(self, token):
        return requests.post(ENDPOINT + '/produtos', json=self, headers={"Authorization": token})

    def update_product(self, _id):
        return requests.put(ENDPOINT + f'/produtos/{_id}', json=self)

    def get_products(self):
        return requests.get(ENDPOINT + '/produtos')

    def delete_product(self):
        return requests.delete(ENDPOINT + f'/produtos/{self}')

    def get_product_by_id(self):
        return requests.get(ENDPOINT + f'/produtos/{self}')
