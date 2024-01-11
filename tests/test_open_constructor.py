from locators import Locators
from helper import log_in, wait_until_visible, wait_until_url_change
from data import URLs


class TestOpenConstructor:

    def test_open_constructor_from_acc(self, driver):
        driver.get(URLs.LOGIN)

        log_in(driver)
        wait_until_visible(driver, Locators.ORDER_BUTTON)

        driver.find_element(*Locators.ACCOUNT_LINK).click()
        wait_until_visible(driver, Locators.ACCOUNT_EMAIL)

        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        constructor_header = wait_until_visible(driver, Locators.H1_HEADER).text

        assert constructor_header == "Соберите бургер"

    def test_open_constructor_from_logo(self, driver):
        driver.get(URLs.LOGIN)

        log_in(driver)
        wait_until_visible(driver, Locators.ORDER_BUTTON)

        driver.find_element(*Locators.ACCOUNT_LINK).click()
        wait_until_visible(driver, Locators.ACCOUNT_EMAIL)

        driver.find_element(*Locators.HEADER_LOGO).click()

        constructor_header = wait_until_visible(driver, Locators.H1_HEADER).text

        assert constructor_header == "Соберите бургер"
