from .base_page import BasePage
from ..locators.main_page_locators import MainPageLocators

import allure

class MainPage(BasePage):

    def create_locator(self, locator, text):
        by, xpath_template = locator
        create_locator = (by, xpath_template.format(text))
        return create_locator

    def create_ID_locator(self, locator, id):
        by, id_template = locator
        final_panel_locator = (by, id_template.format(id))
        return final_panel_locator
        
    @allure.step("Раскрытие {question_text} и проверка соответствия текста ответа")
    def open_accordion_and_check_answer(self, question_text):

        # Создание локатора из шаблона
        question_locator = self.create_locator(MainPageLocators.ACCORDION_HEADER_TEMPLATE, question_text)
        self.wait_for_visible_element(question_locator)
        # Скролл до вопроса и клик
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)

        # Находим кнопку
        header = self.wait_for_visible_element(question_locator)
        
        # Получение ID панели из атрибута aria-controls
        panel_id = header.get_attribute("aria-controls")
            
        # Создание локатора из полученого ID
        final_panel_locator = self.create_locator(MainPageLocators.ACCORDION_PANEL_BY_ID, panel_id)

        self.wait_for_visible_element(final_panel_locator)
        panel_element = self.driver.find_element(*final_panel_locator)

        return panel_element.text.strip()
    