from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    @allure.step("Инициализируем браузер")
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Открываем нужный URL")
    def navigate (self, url):
        self.driver.get(url)

    @allure.step("Ищем нужный элемент")
    def find_element(self, locator, timeout=60):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Ищем нужные элементы")
    def find_elements(self, locator, timeout = 60):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step("Кликаем по нужному элементу")
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step("Заполняем поле нужным значением")
    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step("Ждём, пока элемент станет видимым")
    def wait_for_element_visible(self, locator, timeout = 60):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Ждём, пока элемент перестанет быть видимым")
    def wait_until_element_invisible(self, locator, timeout = 60):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Ждём, пока элемент станет кликабельным")
    def wait_for_element_clickable(self, locator, timeout = 60):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидаем изменения URL на нужный")
    def wait_for_url_change(self, expected_url, timeout=60):
            return WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))

    @allure.step("Перетаскиваем элемент")
    def drag_and_drop(self, source_element, target_element):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    @allure.step("Скроллим")
    def scroll_to_bottom(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)