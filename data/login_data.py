class DataLogin:

    @staticmethod
    def new_login_payload(email, password):

        return {
            "email": email,
            "password": password
        }
