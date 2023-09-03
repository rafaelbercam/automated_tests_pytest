from random import randrange
from faker import Faker


faker = Faker()


class DataProduct:

    @staticmethod
    def new_product_payload():
        job = faker.job()
        return {
            "nome": faker.bothify(text='Product Number: ????-########'),
            "preco": randrange(0, 400, 2),
            "descricao": f"Awsome product for {job} professionals",
            "quantidade": randrange(0, 101, 2)
        }
