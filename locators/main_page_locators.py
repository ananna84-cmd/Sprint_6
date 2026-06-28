from selenium.webdriver.common.by import By

class MainPageLocators:

    # Шаблон: {question} заменится на текст из словаря
    ACCORDION_HEADER_TEMPLATE = (By.XPATH, "//div[contains(@id, 'accordion__heading') and contains(., '{}')]")
    
    # Статичный локатор для панели
    ACCORDION_PANEL_BY_ID = (By.ID, "{}") 

    MAIN_PAGE_LETTER = (By.CSS_SELECTOR, 'div[class*="Home_Header"]')
