import allure
from locators import OrderCreatedLocators
from pages.base_page import BasePage

class OrderCreatedPage(BasePage):

    @allure.step("Ожидаем видимости текста в попапе")
    def wait_until_popup_text_visible(self):
        self.wait_for_element_visible(OrderCreatedLocators.POPUP_TEXT)

    @allure.step("Закрываем попап с информацией о создании заказа")
    def close_order_created_popup(self):
        self.click_element(OrderCreatedLocators.CLOSE_BUTTON)

    @allure.step("Ждём, что кнопка Крестик кликабельна")
    def wait_close_button_clickable(self):
        self.wait_for_element_clickable(OrderCreatedLocators.CLOSE_BUTTON)

    @allure.step("Убеждаемся, что отображается правильный номер заказа, а не 9999")
    def incorrect_number_invisible(self):
        self.wait_until_element_invisible(OrderCreatedLocators.INCORRECT_NUMBER)

    @allure.step("Получаем номер созданного заказа")
    def get_just_created_orders_count(self):
        just_created = self.wait_for_element_visible(OrderCreatedLocators.JUST_CREATED_ORDER)
        return int(just_created.text)