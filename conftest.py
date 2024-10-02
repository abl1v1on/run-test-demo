import pytest
from typing import Generator
from selenium import webdriver


@pytest.fixture
def browser() -> Generator:
    chrome_browser = webdriver.Chrome()
    chrome_browser.maximize_window()
    yield chrome_browser
    chrome_browser.quit()
