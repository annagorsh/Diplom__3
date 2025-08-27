import allure
from links import ORDER_HISTORY_URL
from locators import OrderHistoryLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):

    @allure.step("Ожидаем перехода на страницу с историей заказов")
    def wait_until_url_is_order_history(self):
        self.wait_for_url_change(ORDER_HISTORY_URL)

    @allure.step("Получаем номер заказа, созданного пользователем")
    def get_order_id(self):
        order_element = self.wait_for_element_visible(OrderHistoryLocators.ORDER_NUMBER)
        order_text = order_element.text.strip()
        order_id = order_text.split('#')[1]

        return order_id
