from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        
    # Перейти по URL
    def get_url(self, url):
        self.driver.get(url)

    # Скроллинг до элемента
    def scroll_to_element(self, locator):
        element = self.wait_for_visible_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def scroll_to_web_element(self, element):
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # Ожидание появления элемента
    def wait_for_visible_element(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))
    
    def wait_for_clickable_element(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator))
    
    #  Кликнуть на элемент
    def click_element(self, locator):
        element = self.wait_for_clickable_element(locator)
        element.click()

    # Вытащить текст
    def get_text(self, locator):
        element = self.wait_for_visible_element(locator)
        row_text = element.text
        clean_text = " ".join(row_text.split())
        return clean_text
        
    # Введение данных в поле 
    def fill_field(self, locator, value):
        element = self.wait_for_visible_element(locator)
        element.send_keys(value)
        
    # Принять куки
    def cookie_assept(self, popup_locator, assept_locator):
      self.wait_for_visible_element(popup_locator)
      self.click_element(assept_locator)

    # Открыть страницу и принять куки
    @allure.step("Открытие страницы {url} и принятие куки")
    def open_site_assept_cookie(self, url,  popup_locator, assept_locator):
        self.get_url(url)
        # Принять куки
        self.cookie_assept(popup_locator, assept_locator)
