from ..locators.order_page_locators import OrderPageLocators
from .base_page import BasePage

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import random
import allure


class OrderPage(BasePage):
    def select_random_from_list(self, locator):
        elements = self.wait.until(expected_conditions.presence_of_all_elements_located(locator))
        random_element = random.choice(elements)
        self.scroll_to_web_element(random_element)
        self.wait.until(expected_conditions.element_to_be_clickable(random_element))
        random_element.click()
        

    def fill_text_field(self, name, surname, address, phone):
        self.fill_field(OrderPageLocators.NAME_FIELD, name)
        self.fill_field(OrderPageLocators.SURNAME_FIELD, surname)
        self.fill_field(OrderPageLocators.ADDRESS_FIELD, address)
        self.fill_field(OrderPageLocators.PHONE_FIELD, phone)

    def select_random_metro_station(self):
        self.click_element(OrderPageLocators.METRO_LIST)
        self.wait_for_visible_element(OrderPageLocators.METRO_DROPDOWN)
        self.select_random_from_list(OrderPageLocators.METRO_ITEMS)


    @allure.step("Заполнение данных для заказа в окне 'Для кого самокат'")
    def fill_step_1(self, name, surname, address, phone):
        self.fill_text_field(name, surname, address, phone)
        self.select_random_metro_station()

    # Выбор чекбокса 
    def choice_checkbox(self, locator):
        self.click_element(locator)

    # Выбор даты
    def select_date_in_calendar(self, locator, date):
        self.fill_field(locator, date)
        day = date.split(".")[0]
        cell_locator = (By.XPATH, f"//div[contains(@class, 'day') and text() = '{day}']")
        cell = self.wait.until(expected_conditions.element_to_be_clickable(cell_locator))
        # 4. Клик по ячейке
        cell.click()
        
    @allure.step("Заполнение данных для заказа в окне 'Про аренду'")
    def fill_step_2(self, data, color, comment):
        # Заполнение поля Когда привезти
        self.select_date_in_calendar(OrderPageLocators.DATA_FIELD, data)
        # Выбор из выподающего списка Срок аренды
        self.click_element(OrderPageLocators.RENTAL_PERIOD_CONTROL)
        self.select_random_from_list(OrderPageLocators.RENTAL_PERIOD_OPTIONS)
        # Клик по чекбоксу
        self.choice_checkbox(color)
        # Заполнение комментарий
        self.fill_field(OrderPageLocators.FIELD_COMMENT, comment)
