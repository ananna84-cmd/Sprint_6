import allure
import pytest

from ..data import ORDER_DATA
from ..pages.order_page import OrderPage


@allure.epic("Страница заказа")
@allure.feature("Заказ самоката")
@allure.story("Заказ самоката с валидными данными")
@pytest.mark.parametrize('data',
    [ORDER_DATA["case_1"], ORDER_DATA["case_2"]],
    ids=["order_from_upper_button", "order_from_middle_button"])
class TestOrderProcess:
    @allure.title("Проверка успешного заказа с валидными данными")
    def test_order_with_valid_data(self, main_page, data):
        order_page = OrderPage(main_page.driver)

        order_page.fill_step_1(
            data["button"], 
            data["name"], 
            data["surname"], 
            data["address"], 
            data["phone"]
        )
        order_page.fill_step_2(
            data["date"], 
            data["color"], 
            data["comment"]
        )

        text = order_page.complete_order()

        with allure.step("Проверка успешного оформления заказа"): 
            assert "Заказ оформлен" in text
