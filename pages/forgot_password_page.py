import faker

from locators import ForgotPasswordLocators
from pages.base_page import *

class ForgotPasswordPage(BasePage):

    @allure.step("Ожидаем видимости надписи 'Вспомнили пароль?'")
    def wait_for_remember_password_visible(self):
        self.wait_for_element_visible(ForgotPasswordLocators.REMEMBER_PASSWORD_BUTTON)

    @allure.step("Ожидаем, что поле станет кликабельным")
    def wait_for_email_field_to_be_clickable(self):
        self.wait_for_element_clickable(ForgotPasswordLocators.EMAIL_FIELD)

    @allure.step("Кликаем на поле email")
    def click_email_field(self):
        self.click_element(ForgotPasswordLocators.EMAIL_FIELD)

    @allure.step("Заполняем поле email")
    def fill_in_email_field(self):
        fake = faker.Faker()
        email = fake.email()
        self.enter_text(ForgotPasswordLocators.EMAIL_FIELD_ACTIVE, email)

    @allure.step("Кликаем на кнопку 'Восстановить'")
    def click_reset_button(self):
        self.click_element(ForgotPasswordLocators.RESET_PASSWORD_BUTTON)
