from links import *
from locators import IngredientPopupLocators, MainPageLocators, OrderCreatedLocators
from pages.ingredient_popup_page import IngredientPopupPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import *
from pages.order_created_popup_page import OrderCreatedPage


class TestMainFunctions:

    @allure.title("Проверяем переход на главную по клику на 'Конструктор'")
    def test_go_to_constructor_page(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.navigate(ORDER_FEED_URL)
        order_feed.click_constructor_button()
        main = MainPage(driver)
        main.wait_until_url_main()
        expected_url = MAIN_URL
        assert driver.current_url == expected_url

    @allure.title("Проверяем переход на ленту заказов по клику на 'Лента заказов'")
    def test_go_to_order_feed_page(self, driver):
        main = MainPage(driver)
        main.navigate(MAIN_URL)
        main.click_order_feed_button()
        order_feed = OrderFeedPage(driver)
        order_feed.wait_for_order_feed_url()
        expected_url = ORDER_FEED_URL
        assert driver.current_url == expected_url

    @allure.title("Проверяем открытие и закрытие попапа с информацией об ингредиенте")
    def test_open_ingredient_info(self, driver):
        main = MainPage(driver)
        main.navigate(MAIN_URL)
        main.wait_for_bun()
        main.click_bun()
        popup = IngredientPopupPage(driver)
        popup.wait_until_popup_header_visible()
        assert "ingredient" in driver.current_url
        popup.close_popup()
        popup.wait_until_popup_invisible()
        assert not driver.find_element(*IngredientPopupLocators.INGREDIENT_HEADER).is_displayed()

    @allure.title("Проверяем добавление ингредиента в заказ и изменение у него каунтера")
    def test_add_ingredient(self, driver):
        main = MainPage(driver)
        main.navigate(MAIN_URL)
        main.ingredient_drag_and_drop()
        main.wait_for_counter_visible()
        assert driver.find_element(*MainPageLocators.FLUO_BUN_COUNTER).is_displayed()

    @allure.title("Проверяем флоу оформления заказа авторизованным пользователем")
    def test_authorized_order_flow(self, driver, registration):
        login_page = LoginPage(driver)
        login_page.navigate(LOGIN_URL)
        login_page.fill_in_email(registration['email'])
        login_page.fill_in_password(registration['password'])
        login_page.click_login_button()
        main_page = MainPage(driver)
        main_page.wait_order_button_visible()
        expected_url = MAIN_URL
        assert driver.current_url == expected_url
        main_page.ingredient_drag_and_drop()
        main_page.wait_for_counter_visible()
        main_page.click_order_button()
        popup = OrderCreatedPage(driver)
        popup.wait_until_popup_text_visible()
        assert driver.find_element(*OrderCreatedLocators.POPUP_TEXT).is_displayed()