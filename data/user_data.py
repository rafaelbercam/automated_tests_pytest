from faker import Faker

faker = Faker()


class DataUser:

    @staticmethod
    def new_user_payload():
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = f'{first_name}.{last_name}@{faker.free_email_domain()}'
        password = faker.md5()
        return {
            "nome": f'{first_name} {last_name}',
            "email": email,
            "password": password,
            "administrador": "true"
        }
