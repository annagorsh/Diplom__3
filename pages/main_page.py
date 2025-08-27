import allure
from links import MAIN_URL
from locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Ожидаем видимости кнопки 'Оформить заказ'")
    def wait_order_button_visible(self):
        self.wait_for_element_visible(MainPageLocators.ORDER_BUTTON)

    @allure.step("Кликаем на кнопку 'Личный кабинет' в хедере сайта")
    def click_profile_button(self):
        self.click_element(MainPageLocators.GO_TO_PROFILE_BUTTON)

    @allure.step("Ожидаем смены URL на главную")
    def wait_until_url_main(self):
        self.wait_for_url_change(MAIN_URL)

    @allure.step("Кликаем на кнопку 'Лента заказов' в хедере сайта")
    def click_order_feed_button(self):
        self.click_element(MainPageLocators.GO_TO_ORDER_FEED_BUTTON)

    @allure.step("Кликаем на ингредиент(Флюоресцентная булка) на главной странице")
    def click_bun(self):
        self.click_element(MainPageLocators.FLUO_BUN)

    @allure.step("Ожидаем видимости карточки ингредиента с булкой")
    def wait_for_bun(self):
        self.wait_for_element_clickable(MainPageLocators.FLUO_BUN)

    def get_source_element(self):
        self.wait_for_element_clickable(MainPageLocators.FLUO_BUN)
        return self.driver.find_element(*MainPageLocators.FLUO_BUN)

    def get_target_element(self):
        self.wait_for_element_visible(MainPageLocators.INGREDIENT_PLACE)
        return self.driver.find_element(*MainPageLocators.INGREDIENT_PLACE)

    @allure.step("Перетаскиваем ингредиент в список ингредиентов")
    def ingredient_drag_and_drop(self):
        source_element = self.get_source_element()
        target_element = self.get_target_element()

        self.drag_and_drop(source_element, target_element)

    @allure.step("Ожидаем видимости каунтера")
    def wait_for_counter_visible(self):
        self.wait_for_element_visible(MainPageLocators.FLUO_BUN_COUNTER)

    @allure.step("Нажимаем на кнопку 'Оформить заказ'")
    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

