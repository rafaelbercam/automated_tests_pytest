import requests

import setup.setup

ENDPOINT = setup.setup.SetupClass.base_url()


class LoginRequests:

    def post_login(self):
        return requests.post(ENDPOINT + '/login', json=self)
