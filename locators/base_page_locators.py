from selenium.webdriver.common.by import By


class BasePageLocators:
    # Логотип Яндекс https://dzen.ru/
    LOGO_YANDEX = (By.CSS_SELECTOR, "a[href='//yandex.ru']")

    # Логотип Самокат https://qa-scooter.praktikum-services.ru/
    LOGO_SCOOTER = (By.CSS_SELECTOR, "a[href='/']")

    # Локатор кнопки "Заказать" (в шапке)
    UPPER_ORDER_BUTTON = (By.CSS_SELECTOR, "div.Header_Nav__AGCXC button")

    # Локатор для нижней кнопки (Заказать/
    MIDDLE_ORDER_BUTTON = (By.CSS_SELECTOR, "div.Home_FinishButton__1_cWm button")
