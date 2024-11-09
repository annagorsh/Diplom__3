import allure
import requests
from links import *
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.profile_page import ProfilePage

class TestProfile:

    @allure.title("Проверяем переход с главной страницы в личный кабинет для авторизованного пользователя")
    def test_go_to_profile(self, driver, payload):
        response = requests.post(CREATE_USER_URL, data=payload)
        assert response.status_code == 200
        email = payload.get("email")
        password = payload.get("password")
        login_page = LoginPage(driver)
        login_page.navigate(LOGIN_URL)
        login_page.fill_in_email(email)
        login_page.fill_in_password(password)
        login_page.click_login_button()
        main_page = MainPage(driver)
        main_page.wait_order_button_visible()
        expected_url = MAIN_URL
        assert driver.current_url == expected_url
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.personal_data_informer_visible()
        expected_url = PROFILE_PAGE_URL
        assert driver.current_url == expected_url
        token = response.json().get("accessToken")
        delete_response = requests.delete(AUTH_USER_URL, headers={"Authorization": token})
        assert delete_response.status_code == 202

    @allure.title("Проверяем, что можно перейти в Историю заказов из Личного кабинета")
    def test_go_to_order_history(self, driver, payload):
        response = requests.post(CREATE_USER_URL, data=payload)
        assert response.status_code == 200
        email = payload.get("email")
        password = payload.get("password")
        login_page = LoginPage(driver)
        login_page.navigate(LOGIN_URL)
        login_page.fill_in_email(email)
        login_page.fill_in_password(password)
        login_page.click_login_button()
        main_page = MainPage(driver)
        main_page.wait_order_button_visible()
        expected_url = MAIN_URL
        assert driver.current_url == expected_url
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.personal_data_informer_visible()
        expected_url = PROFILE_PAGE_URL
        assert driver.current_url == expected_url
        profile_page.click_order_history()
        history_page = OrderHistoryPage(driver)
        history_page.wait_until_url_is_order_history()
        expected_url = ORDER_HISTORY_URL
        assert driver.current_url == expected_url
        token = response.json().get("accessToken")
        delete_response = requests.delete(AUTH_USER_URL, headers={"Authorization": token})
        assert delete_response.status_code == 202

    @allure.title("Проверяем, что через личный кабинет можно успешно разлогиниться")
    def test_logout(self, driver, payload):
        response = requests.post(CREATE_USER_URL, data=payload)
        assert response.status_code == 200
        email = payload.get("email")
        password = payload.get("password")
        login_page = LoginPage(driver)
        login_page.navigate(LOGIN_URL)
        login_page.fill_in_email(email)
        login_page.fill_in_password(password)
        login_page.click_login_button()
        main_page = MainPage(driver)
        main_page.wait_order_button_visible()
        expected_url = MAIN_URL
        assert driver.current_url == expected_url
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.personal_data_informer_visible()
        expected_url = PROFILE_PAGE_URL
        assert driver.current_url == expected_url
        profile_page.click_logout()
        profile_page.wait_for_login_url()
        expected_url = LOGIN_URL
        assert driver.current_url == expected_url
        token = response.json().get("accessToken")
        delete_response = requests.delete(AUTH_USER_URL, headers={"Authorization": token})
        assert delete_response.status_code == 202