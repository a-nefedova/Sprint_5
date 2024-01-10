from locators import Locators
from helper import log_in, wait_until_visible, wait_until_url_change
from data import URLs


class TestLogout:

    def test_logout_login_button(self, driver):
        driver.get(URLs.LOGIN)

        log_in(driver)
        wait_until_visible(driver, Locators.ORDER_BUTTON)

        driver.find_element(*Locators.ACCOUNT_LINK).click()
        wait_until_visible(driver, Locators.ACCOUNT_EMAIL)

        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        wait_until_url_change(driver, URLs.ACCOUNT)

        assert driver.current_url == URLs.LOGIN
