from ..data import MAIN_PAGE, YANDEX_PAGE
from ..locators.base_page_locators import BasePageLocators
from ..locators.main_page_locators import MainPageLocators

from selenium.webdriver.support import expected_conditions
import allure

@allure.epic("Главная страница: хэдер")
@allure.feature("Логотипы")
@allure.story("Проверка соответствия действий при нажатии на логотипы")
class TestLogoNavigation:
    @allure.title("Проверка перехода на главную страницу 'Самоката' при нажатии на логотип 'Самоката'")
    def test_yandex_logo_navigation(self,base_page):
        base_page.open_site_assept_cookie(MAIN_PAGE, BasePageLocators.COOKIE_POPUP, BasePageLocators.COOKIE_BUTTON)
        base_page.click_element(BasePageLocators.LOGO_SCOOTER)
        header_element = base_page.get_text(MainPageLocators.MAIN_PAGE_LETTER)
        with allure.step("Проверка перехода на Главную страницу"):
            assert "Самокат на пару дней" in header_element
    @allure.title("Проверка перехода на главную страницу Дзена при нажатии на логотип Яндекса")
    def test_scooter_logo_navigation(self, base_page, driver):
        driver = base_page.driver
        base_page.open_site_assept_cookie(MAIN_PAGE, BasePageLocators.COOKIE_POPUP, BasePageLocators.COOKIE_BUTTON)
        wait = base_page.wait

        # Запоминаем, где мы были ДО клика
        original_window = driver.current_window_handle
        base_page.click_element(BasePageLocators.LOGO_YANDEX)
        wait.until(lambda d: len(d.window_handles) > 1)
                   
        # Переключение на новую вкладку
        new_window = [w for w in driver.window_handles if w != original_window][0]
        driver.switch_to.window(new_window)
        wait.until(expected_conditions.url_contains(YANDEX_PAGE))
        with allure.step("Проверка перехода на Дзен"): 
            assert YANDEX_PAGE in driver.current_url
        