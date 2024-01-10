from locators import Locators
from helper import log_in, wait_until_visible
from data import URLs, Creds


class TestLogin:

    def test_login_from_homepage(self, driver):
        driver.get(URLs.HOMEPAGE)

        wait_until_visible(driver, Locators.LOGIN_ACC_BUTTON)
        driver.find_element(*Locators.LOGIN_ACC_BUTTON).click()

        log_in(driver)
        wait_until_visible(driver, Locators.ORDER_BUTTON)

        driver.quit()

    def test_login_from_account(self, driver):
        driver.get(URLs.ACCOUNT)

        log_in(driver)
        wait_until_visible(driver, Locators.ORDER_BUTTON, 'Не удалось авторизоваться')

        driver.quit()

    def test_login_from_register_form(self, driver):
        driver.get(URLs.REGISTER)

        wait_until_visible(driver, Locators.LOGIN_LINK)
        driver.find_element(*Locators.LOGIN_LINK).click()

        log_in(driver)
        wait_until_visible(driver, Locators.ORDER_BUTTON, 'Не удалось авторизоваться')

        driver.quit()

    def test_login_from_forgot_pass_form(self, driver):
        driver.get(URLs.FORGOT_PASS)

        wait_until_visible(driver, Locators.LOGIN_LINK)
        driver.find_element(*Locators.LOGIN_LINK).click()

        log_in(driver)
        wait_until_visible(driver, Locators.ORDER_BUTTON, 'Не удалось авторизоваться')

        driver.quit()
