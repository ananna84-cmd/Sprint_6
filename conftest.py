import pytest

from selenium import webdriver
from .pages.order_page import OrderPage
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)

@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    yield page

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    yield page

@pytest.fixture
def base_page(driver):
    page = BasePage(driver)
    yield page
