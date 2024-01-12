from locators import Locators
from helper import log_in_and_get_to_acc, wait_until_url_change
from data import URLs


class TestLogout:

    def test_logout_login_url(self, driver):
        driver.get(URLs.LOGIN)

        log_in_and_get_to_acc(driver)

        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        wait_until_url_change(driver, URLs.LOGGED_ACCOUNT)

        assert driver.current_url == URLs.LOGIN
