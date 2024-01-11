from locators import Locators
from data import Creds
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_until_visible(driver, locator):
    return WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locator))


def wait_until_url_change(driver, url):
    WebDriverWait(driver, 5).until(expected_conditions.url_changes(url))


def log_in(driver, email=Creds.email):
    wait_until_visible(driver, Locators.LOGIN_BUTTON)
    driver.find_element(*Locators.EMAIL).send_keys(email)
    driver.find_element(*Locators.PASSWORD).send_keys(Creds.password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()


def switch_to_tab(driver, tab_locator):
    if wait_until_visible(driver, Locators.CURRENT_TAB).text == driver.find_element(*tab_locator).text:
        driver.find_element(*Locators.UNSELECTED_TAB).click()
        assert driver.find_element(*Locators.CURRENT_TAB).text != driver.find_element(*tab_locator).text
    driver.find_element(*tab_locator).click()
