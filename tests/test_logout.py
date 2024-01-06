from locators import Locators
from helper import log_in
import data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogout:
    def test_logout_login_button(self, driver):
        driver.get(f'{data.stellar_burgers_url}/login')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        log_in(driver)
        driver.find_element(*Locators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT_EMAIL))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        login_button_presence = bool(driver.find_elements(*Locators.LOGIN_BUTTON))
        driver.quit()
        assert login_button_presence
