from locators import Locators
from helper import log_in
import data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestOpenAccount:
    def test_open_account_creds(self, driver):
        driver.get(f'{data.stellar_burgers_url}/login')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        log_in(driver)
        driver.find_element(*Locators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT_EMAIL))
        account_email_presence = bool(driver.find_elements(*Locators.ACCOUNT_EMAIL))
        driver.quit()
        assert account_email_presence
