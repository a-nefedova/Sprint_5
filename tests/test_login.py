from locators import Locators
from helper import log_in
import data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def test_login_homepage_order_button(self, driver):
        driver.get(data.stellar_burgers_url)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_ACC_BUTTON))
        driver.find_element(*Locators.LOGIN_ACC_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        log_in(driver)
        order_button_presence = bool(driver.find_elements(*Locators.ORDER_BUTTON))
        driver.quit()
        assert order_button_presence

    def test_login_account_order_button(self, driver):
        driver.get(f'{data.stellar_burgers_url}/account')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        log_in(driver)
        order_button_presence = bool(driver.find_elements(*Locators.ORDER_BUTTON))
        driver.quit()
        assert order_button_presence

    def test_login_register_order_button(self, driver):
        driver.get(f'{data.stellar_burgers_url}/register')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_LINK))
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        log_in(driver)
        order_button_presence = bool(driver.find_elements(*Locators.ORDER_BUTTON))
        driver.quit()
        assert order_button_presence

    def test_login_forgot_pass_order_button(self, driver):
        driver.get(f'{data.stellar_burgers_url}/forgot-password')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_LINK))
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        log_in(driver)
        order_button_presence = bool(driver.find_elements(*Locators.ORDER_BUTTON))
        driver.quit()
        assert order_button_presence
