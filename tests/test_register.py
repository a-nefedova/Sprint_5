from locators import Locators
from helper import log_in, wait_until_visible, enter_register_creds
from data import URLs, Creds


class TestRegister:

    def test_register_enter_valid_creds(self, driver):
        driver.get(URLs.HOMEPAGE)

        wait_until_visible(driver, Locators.LOGIN_ACC_BUTTON).click()
        wait_until_visible(driver, Locators.REG_LINK).click()

        enter_register_creds(driver)
        driver.find_element(*Locators.REG_BUTTON).click()

        log_in(driver, Creds.temp_email)
        basket_button = wait_until_visible(driver, Locators.BASKET_BUTTON).text

        assert basket_button == 'Оформить заказ'

    def test_register_enter_invalid_pass(self, driver):
        driver.get(URLs.HOMEPAGE)

        wait_until_visible(driver, Locators.LOGIN_ACC_BUTTON).click()
        wait_until_visible(driver, Locators.REG_LINK).click()

        enter_register_creds(driver, password='12345')
        driver.find_element(*Locators.REG_BUTTON).click()

        alert_presence = bool(driver.find_elements(*Locators.INVALID_PASS_ALERT))

        assert alert_presence
