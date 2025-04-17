import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options


# Настройка размера окна браузера
@pytest.fixture()
def browser_config():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('window-size=1920,1080')
    browser.config.driver_options = options
    browser.config.base_url = "https://demoqa.com"