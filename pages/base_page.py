from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        
    @allure.step("Переход по {url}")
    def get_url(self, url):
        self.driver.get(url)

    @allure.step("Получение текущего URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Скроллинг до локатора")
    def scroll_to_element(self, locator):
        element = self.wait_for_visible_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Скроллинг до элемента")
    def scroll_to_web_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Ожидание появления элемента")
    def wait_for_visible_element(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))
    
    @allure.step("Ожидание кликабильности элемента")
    def wait_for_clickable_element(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator))
    
    @allure.step("Клик по элементу")
    def click_element(self, locator):
        element = self.wait_for_clickable_element(locator)
        element.click()

    @allure.step("Получение текста")
    def get_text(self, locator):
        element = self.wait_for_visible_element(locator)
        row_text = element.text
        clean_text = " ".join(row_text.split())
        return clean_text
        
    @allure.step("Введение данных в поле")
    def fill_field(self, locator, value):
        element = self.wait_for_visible_element(locator)
        element.send_keys(value)
