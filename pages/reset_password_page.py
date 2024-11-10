import allure
from locators import ResetPasswordLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step("Инициализируем браузер")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидаем видимости поля для ввода кода из имейла")
    def wait_until_email_code_field_is_visible(self):
        self.wait_for_element_visible(ResetPasswordLocators.EMAIL_CODE_FIELD)

    @allure.step("Кликаем в поле 'Пароль'")
    def click_password_field(self):
        self.click_element(ResetPasswordLocators.NEW_PASSWORD_FIELD)

    @allure.step("Ожидаем видимости поля 'Пароль'")
    def wait_until_password_field_visible(self):
        self.wait_for_element_visible(ResetPasswordLocators.NEW_PASSWORD_FIELD)

    @allure.step("Убеждаемся, что значение в поле 'Пароль' стало видимым")
    def is_password_text(self):
        field = self.find_element(ResetPasswordLocators.PASSWORD_FIELD2)
        return field.get_attribute("type") == "text"

    @allure.step("Ищем кнопку в виде глаза")
    def find_password_field_type_text(self):
        self.find_element(ResetPasswordLocators.VIEW_PASSWORD_BUTTON)

    @allure.step("Кликаем на иконку в виде глаза")
    def click_eye_button(self):
        self.click_element(ResetPasswordLocators.VIEW_PASSWORD_BUTTON)