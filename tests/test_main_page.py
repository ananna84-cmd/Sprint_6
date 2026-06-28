import allure
import pytest

from ..data import MAIN_PAGE, FAQ_DATA
from ..locators.base_page_locators import BasePageLocators


class TestMainPageFAQ:

    # Тест на проверку соответствия текста ожидаемому
    @pytest.mark.parametrize(
        "question, expected_answer",
        FAQ_DATA.items(),
        ids=[str(i) for i in range(1, len(FAQ_DATA) + 1)]
    )
    @allure.epic("Главная страница")
    @allure.feature("Блок 'Вопросы о важном': выпадающий список (аккордеон)")
    @allure.story("Проверка соответствия текстов ответов в аккордеоне ожидаемым значениям")
    @allure.title("'Вопросы о важном': проверка соответствия ответа для вопроса '{question}'")
    def test_check_text_in_accordion(self, base_page, main_page, question, expected_answer):
        # Загрузка страницы
        base_page.open_site_assept_cookie(MAIN_PAGE, BasePageLocators.COOKIE_POPUP, BasePageLocators.COOKIE_BUTTON)

        actual_answer = main_page.open_accordion_and_check_answer(question)

        with allure.step("Сравнение полученого текста с ожидаемым"):
            assert expected_answer in actual_answer
