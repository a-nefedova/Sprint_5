from locators import Locators
from data import Creds
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_until_visible(driver, locator):
    return WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locator))


def wait_until_url_change(driver, url):
    WebDriverWait(driver, 5).until(expected_conditions.url_changes(url))


def enter_register_creds(driver, password=Creds.password):
    wait_until_visible(driver, Locators.REG_BUTTON)
    driver.find_element(*Locators.USER_NAME).send_keys(Creds.name)
    driver.find_element(*Locators.EMAIL).send_keys(Creds.temp_email)
    driver.find_element(*Locators.PASSWORD).send_keys(password)


def log_in(driver, email=Creds.email):
    wait_until_visible(driver, Locators.LOGIN_BUTTON)
    driver.find_element(*Locators.EMAIL).send_keys(email)
    driver.find_element(*Locators.PASSWORD).send_keys(Creds.password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()


def log_in_and_get_to_acc(driver):
    log_in(driver)
    wait_until_visible(driver, Locators.ORDER_BUTTON)
    driver.find_element(*Locators.ACCOUNT_LINK).click()
    wait_until_visible(driver, Locators.ACCOUNT_EMAIL)


def switch_to_tab(driver, tab_locator):
    target_tab = driver.find_element(*tab_locator)

    if driver.find_element(*Locators.CURRENT_TAB).text == target_tab.text:
        driver.find_element(*Locators.UNSELECTED_TAB).click()
        assert driver.find_element(*Locators.CURRENT_TAB).text != target_tab.text

    target_tab.click()
