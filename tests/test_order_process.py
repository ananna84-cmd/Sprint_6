import allure
import pytest

from ..data import MAIN_PAGE, ORDER_DATA
from ..locators.base_page_locators import BasePageLocators
from ..locators.order_page_locators import OrderPageLocators



@allure.epic("Страница заказа")
@allure.feature("Заказ самоката")
@allure.story("Заказ самоката с валидными данными")
@pytest.mark.parametrize('order_button, name_button, data',
    [
        (BasePageLocators.UPPER_ORDER_BUTTON, "UPPER_ORDER_BUTTON'", ORDER_DATA["case_1"]),
        (BasePageLocators.MIDDLE_ORDER_BUTTON, "MIDDLE_ORDER_BUTTON", ORDER_DATA["case_2"])
    ],
    ids = ["order_from_upper_button", "order_from_middle_button"])
class TestOrderProcess:
    @allure.title("Проверка заказа через {name_button}")
    def test_order_with_valid_data(self, base_page, order_page, order_button, data, name_button):
        # Загрузка сайта и принятие куки
        base_page.open_site_assept_cookie(MAIN_PAGE, BasePageLocators.COOKIE_POPUP, BasePageLocators.COOKIE_BUTTON)
        # Кликнуть на кнопку Заказать
        base_page.click_element(order_button)
        # Ожидание 1 окна
        base_page.wait_for_visible_element(OrderPageLocators.NAME_FIELD)

        # Заполнить 1 форму
        order_page.fill_step_1(data["name"], data["surname"], data["address"], data["phone"])

        # кликнуть кнопку Далее
        base_page.click_element(OrderPageLocators.NEXT_BUTTON)
        # Ожидание 2 окна
        base_page.wait_for_visible_element(OrderPageLocators.DATA_FIELD)

        # Заполнить 2 форму
        order_page.fill_step_2(data["date"], data["color"], data["comment"])

        # Кликнуть кнопку Заказать
        base_page.click_element(OrderPageLocators.ORDER_BUTTON)     

        base_page.wait_for_visible_element(OrderPageLocators.YES_BUTTON)
        order_page.click_element(OrderPageLocators.YES_BUTTON)

        # Ожидание текста подтверждения
        base_page.wait_for_visible_element(OrderPageLocators.ORDER_POPUP)
        # Вытащить текст сравнить с ожидаемым
        text = order_page.get_text(OrderPageLocators.ORDER_STATUS_MESSAGE)
        with allure.step("Проверка что заказ успешно оформлен"): 
            assert "Заказ оформлен" in text
