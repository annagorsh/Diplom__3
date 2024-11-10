import allure
from links import *
from locators import OrderPopupFeedLocators, OrderFeedLocators, OrderCreatedLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.order_history_page import OrderHistoryPage
from pages.order_popup_feed_page import OrderPopupFeedPage
from pages.order_created_popup_page import OrderCreatedPage
from pages.profile_page import ProfilePage


class TestOrderFeed:

    @allure.title("Проверяем, что по клику на заказ открывается попап с его деталями")
    def test_open_order_info_popup_opens(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.navigate(ORDER_FEED_URL)
        order_feed.wait_for_order_feed_header()
        order_feed.click_order()
        popup = OrderPopupFeedPage(driver)
        popup.wait_until_contents_visible()
        assert driver.find_element(*OrderPopupFeedLocators.CONTENTS_HEADER).is_displayed()

    @allure.title("Проверяем, что заказы пользователя из раздела 'История заказов' отображаются в ленте")
    def test_users_orders_displayed_in_feed(self, driver, registration):
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
        popup.incorrect_number_invisible()
        popup.close_order_created_popup()
        main = MainPage(driver)
        main.click_profile_button()
        profile = ProfilePage(driver)
        profile.personal_data_informer_visible()
        profile.click_order_history()
        history_page = OrderHistoryPage(driver)
        history_page.wait_until_url_is_order_history()
        order_id = history_page.get_order_id()
        orders_feed = OrderFeedPage(driver)
        orders_feed.navigate(ORDER_FEED_URL)
        specific_order_locator = (OrderFeedLocators.SPECIFIC_ORDER_LOCATOR[0], OrderFeedLocators.SPECIFIC_ORDER_LOCATOR[1].format(order_id))
        element = orders_feed.wait_for_element_visible(specific_order_locator)
        assert element.is_displayed()

    @allure.title("Проверяем, что при создании заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_alltime_orders_increased(self, driver, registration):
        login_page = LoginPage(driver)
        login_page.navigate(LOGIN_URL)
        login_page.fill_in_email(registration['email'])
        login_page.fill_in_password(registration['password'])
        login_page.click_login_button()
        main_page = MainPage(driver)
        main_page.wait_order_button_visible()
        expected_url = MAIN_URL
        assert driver.current_url == expected_url
        main_page.click_order_feed_button()
        order_feed = OrderFeedPage(driver)
        order_feed.wait_for_order_feed_header()
        result = order_feed.get_completed_orders_count()
        order_feed.click_constructor_button()
        main = MainPage(driver)
        main.wait_order_button_visible()
        main.ingredient_drag_and_drop()
        main.click_order_button()
        popup = OrderCreatedPage(driver)
        popup.incorrect_number_invisible()
        popup.close_order_created_popup()
        main_return = MainPage(driver)
        main_return.click_order_feed_button()
        order_feed_return = OrderFeedPage(driver)
        new_result = order_feed_return.get_completed_orders_count()
        assert new_result == result + 1

    @allure.title("Проверяем, что при создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_todays_orders_increased(self, driver, registration):
        login_page = LoginPage(driver)
        login_page.navigate(LOGIN_URL)
        login_page.fill_in_email(registration['email'])
        login_page.fill_in_password(registration['password'])
        login_page.click_login_button()
        main_page = MainPage(driver)
        main_page.wait_order_button_visible()
        expected_url = MAIN_URL
        assert driver.current_url == expected_url
        main_page.click_order_feed_button()
        order_feed = OrderFeedPage(driver)
        order_feed.wait_for_order_feed_header()
        order_feed.scroll_to_todays_counter()
        result = order_feed.get_todays_orders_count()
        order_feed.click_constructor_button()
        main = MainPage(driver)
        main.wait_order_button_visible()
        main.ingredient_drag_and_drop()
        main.click_order_button()
        popup = OrderCreatedPage(driver)
        popup.incorrect_number_invisible()
        popup.close_order_created_popup()
        main_return = MainPage(driver)
        main_return.click_order_feed_button()
        order_feed_return = OrderFeedPage(driver)
        order_feed_return.scroll_to_todays_counter()
        new_result = order_feed_return.get_todays_orders_count()
        assert new_result == result + 1

    @allure.title("Проверяем отображение созданного заказа в разделе В работе")
    def test_created_order_in_work(self, driver, registration):
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
        main_page.click_order_button()
        popup = OrderCreatedPage(driver)
        popup.incorrect_number_invisible()
        result = popup.get_just_created_orders_count()
        popup.close_order_created_popup()
        main_return = MainPage(driver)
        main_return.click_order_feed_button()
        order_feed = OrderFeedPage(driver)
        order_feed.wait_for_order_feed_header()
        specific_locator = OrderCreatedLocators.WAITING_FOR[0], OrderCreatedLocators.WAITING_FOR[1].format(result)
        element = order_feed.wait_for_element_visible(specific_locator, timeout=999)
        assert element.is_displayed()
