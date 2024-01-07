from locators import Locators
from helper import log_in, wait_until_visible
import data


class TestLogin:

    def test_login_from_homepage(self, driver):
        driver.get(data.stellar_burgers_url)

        wait_until_visible(driver, Locators.LOGIN_ACC_BUTTON)
        driver.find_element(*Locators.LOGIN_ACC_BUTTON).click()

        log_in(driver)
        wait_until_visible(driver, Locators.ORDER_BUTTON, 'Не удалось авторизоваться')

        driver.quit()

    def test_login_from_account(self, driver):
        driver.get(f'{data.stellar_burgers_url}/account')

        log_in(driver)
        wait_until_visible(driver, Locators.ORDER_BUTTON, 'Не удалось авторизоваться')

        driver.quit()

    def test_login_from_register_form(self, driver):
        driver.get(f'{data.stellar_burgers_url}/register')

        wait_until_visible(driver, Locators.LOGIN_LINK)
        driver.find_element(*Locators.LOGIN_LINK).click()

        log_in(driver)
        wait_until_visible(driver, Locators.ORDER_BUTTON, 'Не удалось авторизоваться')

        driver.quit()

    def test_login_from_forgot_pass_form(self, driver):
        driver.get(f'{data.stellar_burgers_url}/forgot-password')

        wait_until_visible(driver, Locators.LOGIN_LINK)
        driver.find_element(*Locators.LOGIN_LINK).click()

        log_in(driver)
        wait_until_visible(driver, Locators.ORDER_BUTTON, 'Не удалось авторизоваться')

        driver.quit()
