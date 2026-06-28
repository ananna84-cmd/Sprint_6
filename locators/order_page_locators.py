from selenium.webdriver.common.by import By

class OrderPageLocators:
    # 1 Страница: "Для кого заказ"
    # Поле Имя
    NAME_FIELD = (By.CSS_SELECTOR, '[placeholder="* Имя"]')
    # Поле Фамилия
    SURNAME_FIELD = (By.CSS_SELECTOR, '[placeholder="* Фамилия"]')
    # Поле Адрес
    ADDRESS_FIELD = (By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')

    # Поле Станция метро
    METRO_FIELD = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')
    # Кнопка "Далее"
    NEXT_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Далее')]")
    # Кнопка "Да"
    YES_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and normalize-space(.)='Да']")
    # Кнопка "Заказать" в окне заказа
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]//button[contains(@class, 'Button_Button__ra12g') and normalize-space(.)='Заказать']")
    # Кнопка "Посмотреть заказ"
    SHOW_OPDER_BUTTON = (By.XPATH, '//div[contains(@class, "Order_NextButton")]//button[contains(@class, "Button_Button") and text()="Посмотреть статус"]')

    # Локатор на сам список
    METRO_LIST = (By.CSS_SELECTOR, "div.select-search__value")
    # Выбренная станция
    METRO_ITEMS = (By.CSS_SELECTOR, "ul.select-search__options li")
    # Локатор для контейнера списка 
    METRO_DROPDOWN = (By.CSS_SELECTOR, "ul[class*='search__options']")
    
    # Поле Телефон
    PHONE_FIELD = (By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]')

    # 2 Страница: "Про аренду"
    # Поле "Когда привезти самокат"
    DATA_FIELD = (By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]')
    # Поле "Срок аренды"
    RENTAL_PERIOD_CONTROL = (By.CSS_SELECTOR, "div.Dropdown-control[aria-haspopup='listbox']")
    RENTAL_PERIOD_OPTIONS = (By.CSS_SELECTOR, "div.Dropdown-option")

    # Поле "Цвет самоката"
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GRAY_COLOR_CHECKBOX = (By.ID, "grey")

    # Поле "Комментарий"
    FIELD_COMMENT = (By.CSS_SELECTOR, '[placeholder="Комментарий для курьера"]')

    # Окно подтверждения заказа/ окно Заказ оформлен
    ORDER_POPUP = (By.CSS_SELECTOR, ".Order_Modal__YZ-d3")

    # Локатор текста в окне заказ оформлен
    ORDER_STATUS_MESSAGE = (By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ")
    # Сам текст "Заказ оформлен"
    DAY_CELL = (By.XPATH, "//div[contains(@class, 'day') and text() = '{}']")
