from selenium.webdriver.common.by import By

class MainPageLocators:
    # Попап Cookie
    COOKIE_POPUP = (By.CSS_SELECTOR, "div.App_CookieConsent__1yUIN")

    # Кнопка Cookie
    COOKIE_BUTTON = (By.CSS_SELECTOR, "button.App_CookieButton__3cvqF")

    # Шаблон: {question} заменится на текст из словаря
    ACCORDION_HEADER_TEMPLATE = (By.XPATH, "//div[contains(@id, 'accordion__heading') and contains(., '{}')]")
    
    # Статичный локатор для панели
    ACCORDION_PANEL_BY_ID = (By.ID, "{}") 

    MAIN_PAGE_LETTER = (By.CSS_SELECTOR, 'div[class*="Home_Header"]')
