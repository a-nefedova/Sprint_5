from locators import Locators
import data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_until_visible(driver, locator, message=""):
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locator), message=message)


def log_in(driver, email=data.email):
    wait_until_visible(driver, Locators.LOGIN_BUTTON)
    driver.find_element(*Locators.EMAIL).send_keys(email)
    driver.find_element(*Locators.PASSWORD).send_keys(data.password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
