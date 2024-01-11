from locators import Locators
from helper import log_in, wait_until_visible
from data import URLs, Creds


class TestRegister:

    def test_register_enter_valid_creds(self, driver):
        driver.get(URLs.HOMEPAGE)

        wait_until_visible(driver, Locators.LOGIN_ACC_BUTTON).click()

        wait_until_visible(driver, Locators.REG_LINK).click()

        wait_until_visible(driver, Locators.REG_BUTTON)
        driver.find_element(*Locators.USER_NAME).send_keys(Creds.name)
        driver.find_element(*Locators.EMAIL).send_keys(Creds.temp_email)
        driver.find_element(*Locators.PASSWORD).send_keys(Creds.password)
        driver.find_element(*Locators.REG_BUTTON).click()

        log_in(driver, Creds.temp_email)
        basket_button = wait_until_visible(driver, Locators.BASKET_BUTTON).text

        assert basket_button == 'Оформить заказ'

    def test_register_enter_short_pass_error(self, driver):
        driver.get(URLs.HOMEPAGE)

        wait_until_visible(driver, Locators.LOGIN_ACC_BUTTON).click()

        wait_until_visible(driver, Locators.REG_LINK).click()

        wait_until_visible(driver, Locators.REG_BUTTON)
        driver.find_element(*Locators.USER_NAME).send_keys(Creds.name)
        driver.find_element(*Locators.EMAIL).send_keys(Creds.temp_email)
        driver.find_element(*Locators.PASSWORD).send_keys('12345')
        driver.find_element(*Locators.REG_BUTTON).click()

        input_error = driver.find_element(*Locators.INPUT_ERROR).text

        assert input_error == "Некорректный пароль"
