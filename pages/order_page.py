from ..locators.order_page_locators import OrderPageLocators
from .base_page import BasePage

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import random
import allure


class OrderPage(BasePage):
    @allure.step("Выбор случайного элемента из списка")
    def select_random_from_list(self, locator):
        elements = self.wait.until(expected_conditions.presence_of_all_elements_located(locator))
        random_element = random.choice(elements)
        self.scroll_to_web_element(random_element)
        self.wait.until(expected_conditions.element_to_be_clickable(random_element))
        random_element.click()
        
    @allure.step("Заполнение данных для заказа: {name}, {surname}, {address}, {phone}")
    def fill_text_field(self, name, surname, address, phone):
        self.fill_field(OrderPageLocators.NAME_FIELD, name)
        self.fill_field(OrderPageLocators.SURNAME_FIELD, surname)
        self.fill_field(OrderPageLocators.ADDRESS_FIELD, address)
        self.fill_field(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step("Выбор случайной станции метро")
    def select_random_metro_station(self):
        self.click_element(OrderPageLocators.METRO_LIST)
        self.wait_for_visible_element(OrderPageLocators.METRO_DROPDOWN)
        self.select_random_from_list(OrderPageLocators.METRO_ITEMS)

    @allure.step("Выбор чекбокса") 
    def choice_checkbox(self, locator):
        self.click_element(locator)

    @allure.step("Выбор даты: {date}")
    def select_date_in_calendar(self, locator, date):
        self.fill_field(locator, date)
        day = date.split(".")[0]
        cell_locator = (By.XPATH, f"//div[contains(@class, 'day') and text() = '{day}']")
        cell = self.wait.until(expected_conditions.element_to_be_clickable(cell_locator))
        cell.click()
        
    @allure.step("Заполнение данных для заказа в окне 'Для кого самокат' и нажатие кнопки Далее")
    def fill_step_1(self, order_button, name, surname, address, phone):
        # Кликнуть на кнопку Заказать
        self.click_element(order_button)
        self.fill_text_field(name, surname, address, phone)
        self.select_random_metro_station()
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение данных для заказа в окне 'Про аренду' и нажатие кнопки Заказать")
    def fill_step_2(self, data, color, comment):
        self.select_date_in_calendar(OrderPageLocators.DATA_FIELD, data)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_CONTROL)
        self.select_random_from_list(OrderPageLocators.RENTAL_PERIOD_OPTIONS)
        self.choice_checkbox(color)
        self.fill_field(OrderPageLocators.FIELD_COMMENT, comment)
        self.click_element(OrderPageLocators.ORDER_BUTTON)     

    @allure.step("Подтверждение заказа: клик по кнопке 'Да' и получение текста статуса")
    def complete_order(self):
        self.click_element(OrderPageLocators.YES_BUTTON)
        text = self.get_text(OrderPageLocators.ORDER_STATUS_MESSAGE)
        return text
