from .pages.main_page import MainPage

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open_site_and_accept_cookies() 
    yield page
    