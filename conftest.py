import pytest
from typing import Generator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_options() -> Options:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    return chrome_options

@pytest.fixture
def browser() -> Generator:
    chrome_browser = webdriver.Chrome(options=get_chrome_options())
    chrome_browser.maximize_window()
    yield chrome_browser
    chrome_browser.quit()
