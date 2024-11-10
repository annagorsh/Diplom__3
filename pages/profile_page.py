import allure
from links import LOGIN_URL
from locators import ProfileLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step("Ожидаем видимости надписи о ПД в личном кабинете")
    def personal_data_informer_visible(self):
        self.wait_for_element_visible(ProfileLocators.PERSONAL_DATA_INFORMER)

    @allure.step("Кликаем на раздел с историей заказов")
    def click_order_history(self):
        self.click_element(ProfileLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Кликаем на кнопку Выход")
    def click_logout(self):
        self.click_element(ProfileLocators.LOGOUT_BUTTON)

    @allure.step("Дожидаемся смены URL на страницу логина")
    def wait_for_login_url(self):
        self.wait_for_url_change(LOGIN_URL)