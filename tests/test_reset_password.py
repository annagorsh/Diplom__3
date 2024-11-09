from links import *
from pages.login_page import *
from pages.forgot_password_page import *
from pages.reset_password_page import *

class TestResetPassword:

    @allure.title("Проверяем, что клик на 'Восстановить пароль' на странице логина ведёт на страницу восстановления пароля")
    def test_click_reset_password_on_login_page(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate(LOGIN_URL)
        login_page.click_reset_password()
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.wait_for_remember_password_visible()
        expected_url = FORGOT_PASSWORD_URL
        assert driver.current_url == expected_url

    @allure.title("Проверяем, что можно ввести email и перейти к восстановлению пароля")
    def test_enter_email_and_go_to_reset_password(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.navigate(FORGOT_PASSWORD_URL)
        forgot_page.wait_for_email_field_to_be_clickable()
        forgot_page.click_email_field()
        forgot_page.fill_in_email_field()
        forgot_page.click_reset_button()
        reset_page = ResetPasswordPage(driver)
        reset_page.wait_until_email_code_field_is_visible()
        expected_url = RESET_PASSWORD_URL
        assert driver.current_url == expected_url

    @allure.title("Проверяем, что по клику на иконку в виде глаза пароль становится видимым")
    def test_draft_2(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.navigate(FORGOT_PASSWORD_URL)
        forgot_page.wait_for_email_field_to_be_clickable()
        forgot_page.click_reset_button()
        reset_page = ResetPasswordPage(driver)
        reset_page.wait_until_password_field_visible()
        expected_url = RESET_PASSWORD_URL
        assert driver.current_url == expected_url
        reset_page.click_password_field()
        reset_page.find_password_field_type_text()
        reset_page.click_eye_button()
        result = reset_page.check_if_password_field_is_text()
        assert result == True