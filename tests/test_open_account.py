from locators import Locators
from helper import log_in, wait_until_visible
from data import URLs, Creds


class TestOpenAccount:

    def test_open_account_creds(self, driver):
        driver.get(URLs.HOMEPAGE)

        log_in(driver)
        wait_until_visible(driver, Locators.ORDER_BUTTON)

        driver.find_element(*Locators.ACCOUNT_LINK).click()
        wait_until_visible(driver, Locators.ACCOUNT_EMAIL)

        assert driver.find_element(*Locators.ACCOUNT_EMAIL).get_attribute("value") == Creds.email
