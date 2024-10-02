from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, browser: WebDriver, timeout: int = 10) -> None:
        self.browser: WebDriver = browser
        self.url: str = 'https://demoqa.com/'
        self.browser.implicitly_wait(timeout)
    
    def open(self) -> None:
        self.browser.get(self.url)
    
    def find(self, *locator) -> WebElement:
        return self.browser.find_element(*locator)
