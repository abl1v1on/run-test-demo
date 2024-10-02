import allure
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages import BasePage


class RegistrationPage(BasePage):
    def __init__(self, browser: WebDriver, timeout: int = 10) -> None:
        super().__init__(browser, timeout)
        self.url = self.url + 'automation-practice-form'

    @property
    def first_name_filed(self) -> WebElement:
        return self.find(By.ID, 'firstName')

    @property
    def last_name_field(self) -> WebElement:
        return self.find(By.ID, 'lastName')

    @property
    def email_field(self) -> WebElement:
        return self.find(By.ID, 'userEmail')

    @property
    def gender_male_radio(self) -> WebElement:
        return self.find(By.XPATH, '//label[@for="gender-radio-1"]')
    
    @property
    def gender_female_radio(self) -> WebElement:
        return self.find(By.XPATH, '//label[@for="gender-radio-2"]')
    
    @property
    def gender_other_radio(self) -> WebElement:
        return self.find(By.XPATH, '//label[@for="gender-radio-3"]')
    
    @property
    def phone_number_field(self) -> WebElement:
        return self.find(By.ID, 'userNumber')
    
    @property
    def date_of_birth_field(self) -> WebElement:
        return self.find(By.ID, 'dateOfBirthInput')
    
    @property
    def subjects_field(self) -> WebElement:
        return self.find(By.ID, 'subjectsInput')
    
    @property
    def hobbie_sports_checkbox(self) -> WebElement:
        return self.find(By.XPATH, '//label[@for="hobbies-checkbox-1"]')
    
    @property
    def hobbie_reading_checkbox(self) -> WebElement:
        return self.find(By.XPATH, '//label[@for="hobbies-checkbox-2"]')
    
    @property
    def hobbie_music_checkbox(self) -> WebElement:
        return self.find(By.XPATH, '//label[@for="hobbies-checkbox-3"]')
    
    @property
    def picture_field(self) -> WebElement:
        return self.find(By.ID, 'uploadPicture')
    
    @property
    def current_address_textarea(self) -> WebElement:
        return self.find(By.ID, 'currentAddress')
    
    @property
    def state_field(self) -> WebElement:
        return self.find(By.ID, 'react-select-3-input')
    
    @property
    def city_field(self) -> WebElement:
        return self.find(By.ID, 'react-select-4-input')
    
    @property
    def submit_button(self) -> WebElement:
        return self.find(By.ID, 'submit')

    @property
    def submitting_form_modal(self) -> WebElement:
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.ID, 'example-modal-sizes-title-lg'))
        )
