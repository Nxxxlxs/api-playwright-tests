import allure


def attach_response(response):

    with allure.step("Salvar response"):
        allure.attach(
            response.text(),
            name="response",
            attachment_type=allure.attachment_type.JSON
        )