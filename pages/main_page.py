from .base_page import BasePage
from ..locators.base_page_locators import BasePageLocators
from ..locators.main_page_locators import MainPageLocators
from ..data import MAIN_PAGE, YANDEX_PAGE

import allure
from selenium.webdriver.support import expected_conditions


class MainPage(BasePage):
            
    @allure.step("Принять куки")
    def cookie_assept(self):
      self.wait_for_visible_element(MainPageLocators.COOKIE_POPUP)
      self.click_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Открытие страницы и принятие куки")
    def open_site_and_accept_cookies(self):
        self.get_url(MAIN_PAGE)
        self.cookie_assept()

    @allure.step("Создать локатор")
    def create_locator(self, locator, text):
        by, xpath_template = locator
        create_locator = (by, xpath_template.format(text))
        return create_locator
        
    @allure.step("Раскрытие {question_text} и проверка соответствия текста ответа")
    def open_accordion_and_check_answer(self, question_text):
        # Создание локатора из шаблона
        question_locator = self.create_locator(MainPageLocators.ACCORDION_HEADER_TEMPLATE, question_text)
        # Скролл до вопроса и клик
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)
        header = self.wait_for_visible_element(question_locator)
        # Получение ID панели из атрибута aria-controls
        panel_id = header.get_attribute("aria-controls")
        # Создание локатора из полученого ID
        final_panel_locator = self.create_locator(MainPageLocators.ACCORDION_PANEL_BY_ID, panel_id)
        self.wait_for_visible_element(final_panel_locator)
        panel_element = self.driver.find_element(*final_panel_locator)
        return panel_element.text.strip()
    
    @allure.step("Переключение на новую вкладку и ожидание {url}")
    def switch_to_new_window_and_wait_url(self, url):
        self.switch_to_new_window()
        self.wait.until(expected_conditions.url_contains(url))

    @allure.title("Получение текста заголовка после клика по логотипу самоката")
    def get_header_text_after_logo_click(self):
        self.click_element(BasePageLocators.LOGO_SCOOTER)
        header_text = self.get_text(MainPageLocators.MAIN_PAGE_LETTER)
        return header_text

    @allure.title("Переход на страницу Яндекса через логотип")
    def navigate_to_yandex_via_logo(self):
        self.click_element(BasePageLocators.LOGO_YANDEX)
        self.switch_to_new_window_and_wait_url(YANDEX_PAGE)
        self.wait.until(expected_conditions.url_contains(YANDEX_PAGE))
        