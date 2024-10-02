import allure
from selenium.webdriver.common.keys import Keys

from pages import RegistrationPage


@allure.feature('Registration')
def test_reg_with_valid_data(browser):
    page = RegistrationPage(browser)
    page.open()

    page.first_name_filed.send_keys('Maxim')
    page.last_name_field.send_keys('Danilov')
    page.email_field.send_keys('abl1v1on@yandex.ru')
    page.gender_male_radio.click()
    page.phone_number_field.send_keys('88005553535')
    page.current_address_textarea.send_keys('Some address value')
    page.state_field.send_keys('NC' + Keys.TAB)
    page.city_field.send_keys('Del' + Keys.TAB)
    page.submit_button.click()

    assert page.submitting_form_modal.is_displayed(), (
        'Не показывается модальное окно при успешной регистрации'
    )
