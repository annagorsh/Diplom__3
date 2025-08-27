from pages.base_page import *
from locators import *
import allure

class LoginPage(BasePage):

    @allure.step("Нажимаем 'Восстановить пароль' на странице логина")
    def click_reset_password(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_BUTTON)

    @allure.step("Заполняем поле Email")
    def fill_in_email(self, text):
        self.wait_for_element_clickable(LoginPageLocators.EMAIL_FIELD_INACTIVE)
        self.click_element(LoginPageLocators.EMAIL_FIELD_INACTIVE)
        self.enter_text(LoginPageLocators.EMAIL_FIELD_ACTIVE, text)

    @allure.step("Заполняем поле 'Пароль'")
    def fill_in_password(self, text):
        self.wait_for_element_clickable(LoginPageLocators.PASSWORD_FIELD_INACTIVE)
        self.click_element(LoginPageLocators.PASSWORD_FIELD_INACTIVE)
        self.enter_text(LoginPageLocators.PASSWORD_FIELD_ACTIVE, text)

    @allure.step("Нажимаем на кнопку 'Войти'")
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)