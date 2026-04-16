import allure

from api.utils.allure_helpers import attach_response

@allure.title("Validar listagem de usuários")
@allure.description("Verifica se API retorna lista de usuários corretamente")
def test_list_users(users):

    with allure.step("Busca os usuários"):
        response = users.list_users()

    attach_response(response)

    with allure.step("Validar resposta"):
        assert response.ok
        data = response.json()

        assert isinstance(data, list)
        assert len(data) > 0

@allure.title("Validar listagem de usuários")
@allure.description("Verifica se API retorna lista de usuários corretamente")
def test_create_user(users):
    payload = {
        "name": "John",
        "email": "john@test.com"
    }

    with allure.step("Cria o usuário"):
        response = users.create_user(payload)

    attach_response(response)

    with allure.step("Validar resposta"):
        assert response.ok