# __Boilerplate API Tests with Pytest__

## __Ambiente__
Para executar os testes localmente, estou utilizando o ServeRest

<p align="left">
 <img alt="Logo do ServeRest" src="https://user-images.githubusercontent.com/29241659/115161869-6a017e80-a076-11eb-9bbe-c391eff410db.png" height="80">
</p>

Link do Repo: https://github.com/ServeRest/ServeRest

ServeRest está disponível de forma [online](https://serverest.dev), no [npm](https://www.npmjs.com/package/serverest) e no [docker](https://hub.docker.com/r/paulogoncalvesbh/serverest/).
```
npm install
```
Para iniciar o serviço basta acessar a pasta ServeRest-trunk rodar o comando
```
npx serverest@latest

```

## Pré Requisitos REST-assured

- [Python 3](https://www.python.org/)


## Instalação

Clone project

- Clone este repositório para sua maquina usando http or ssh, por exemplo:

`git clone https://github.com/rafaelbercam/automated_tests_pytest`

- Instale todas as dependências:


`pip install`

## __Rodar os testes__
Basta rodar o comando
```
pytest --html=report.html --self-contained-html  
```

## __Configuração do Projeto__

O projeto esta dividido da seguinte maneira:



        [automated_tests_pytest]
           [data] -> Classe Python responsável por criar objetos (payload) para as requisições
           [services] -> Classe que possui funções que retornam as requisições para a camada de testes
           [setup] -> Classe para configurar variáveis, constrantes sobre o ambiente de testes
           [tests] -> Classes de teste do Pytest


### __data__
São classes que retornam objetos de acordo com os paramentros enviados em uma requisição.

Exemplo:

```python
class DataUser:

    @staticmethod
    def new_user_payload():
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = f'{first_name}.{last_name}@email.com'
        password = faker.md5()
        return {
            "nome": f'{first_name} {last_name}',
            "email": email,
            "password": password,
            "administrador": "true"
        }

```

### __services__

Em `services`, retornam a `Response` da requisição.

Exemplo da Classe:

```python
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

```


### __test__
Em ``tests``, poderão ser colocados os arquivos de teste no formato do Pytest.


Exemplo da classe:

```python

class TestUsers:

    def test_get_users(self):
        get_response = request.get_user(None)
        assert get_response.status_code == 200

    def test_post_user(self):
        user_payload = user_data.new_user_payload()
        post_response = request.create_user(user_payload)
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

```
