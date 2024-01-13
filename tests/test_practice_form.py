from data.user_data import user
from pages.registration_page import RegistrationPage
import allure


def test_add_form():
    registration_page = RegistrationPage()

    with allure.step('Открываем тестируемую форму https://demoqa.com/automation-practice-form'):
        registration_page.open()

    with allure.step('Заполняем форму'):
        registration_page.fill_form(user)

    with allure.step('Проверяем форму'):
        registration_page.assert_form(user)
