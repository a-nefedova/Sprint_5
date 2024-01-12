from locators import Locators
from helper import log_in, wait_until_visible
from data import URLs


class TestLogin:

    def test_login_from_homepage(self, driver):
        driver.get(URLs.HOMEPAGE)

        basket_button_before = wait_until_visible(driver, Locators.BASKET_BUTTON).text
        driver.find_element(*Locators.LOGIN_ACC_BUTTON).click()

        log_in(driver)
        basket_button_after = wait_until_visible(driver, Locators.BASKET_BUTTON).text

        assert (basket_button_after != basket_button_before) and (basket_button_after == 'Оформить заказ')

    def test_login_from_account(self, driver):
        driver.get(URLs.ACCOUNT)

        log_in(driver)
        basket_button = wait_until_visible(driver, Locators.BASKET_BUTTON).text

        assert basket_button == 'Оформить заказ'

    def test_login_from_register_form(self, driver):
        driver.get(URLs.REGISTER)

        driver.find_element(*Locators.LOGIN_LINK).click()

        log_in(driver)
        basket_button = wait_until_visible(driver, Locators.BASKET_BUTTON).text

        assert basket_button == 'Оформить заказ'

    def test_login_from_forgot_pass_form(self, driver):
        driver.get(URLs.FORGOT_PASS)

        wait_until_visible(driver, Locators.LOGIN_LINK).click()

        log_in(driver)
        basket_button = wait_until_visible(driver, Locators.BASKET_BUTTON).text

        assert basket_button == 'Оформить заказ'
