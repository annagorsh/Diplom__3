import allure
from locators import OrderPopupFeedLocators
from pages.base_page import BasePage

class OrderPopupFeedPage(BasePage):

    @allure.step("Ожидаем видимости надписи Состав в попапе")
    def wait_until_contents_visible(self):
        self.wait_for_element_visible(OrderPopupFeedLocators.CONTENTS_HEADER)