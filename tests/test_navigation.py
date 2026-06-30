from ..data import YANDEX_PAGE

import allure


@allure.epic("Главная страница: хэдер")
@allure.feature("Логотипы")
@allure.story("Проверка соответствия действий при нажатии на логотипы")
class TestLogoNavigation:
    @allure.title("Проверка перехода на главную страницу 'Самоката' при нажатии на логотип 'Самоката'")
    def test_scooter_logo_navigation(self, main_page):
        header_text = main_page.get_header_text_after_logo_click()
        with allure.step("Проверка перехода на Главную страницу"):
            assert "Самокат на пару дней" in header_text

    @allure.title("Проверка перехода на главную страницу Дзена при нажатии на логотип Яндекса")
    def test_yandex_logo_navigation(self, main_page):
        main_page.navigate_to_yandex_via_logo()
        current_url = main_page.get_current_url()
        
        with allure.step("Проверка перехода на страницу Дзена"): 
            assert YANDEX_PAGE in current_url
        