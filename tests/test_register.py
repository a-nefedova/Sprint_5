from locators import Locators
from helper import log_in
import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegister:
    def test_register_enter_creds_order_button(self, driver):  # TODO ******** replace 77777 to 4 *********
        driver.get(data.stellar_burgers_url)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_ACC_BUTTON))
        driver.find_element(*Locators.LOGIN_ACC_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REG_LINK))
        driver.find_element(*Locators.REG_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REG_BUTTON))
        driver.find_element(*Locators.USER_NAME).send_keys(data.name)
        driver.find_element(*Locators.EMAIL).send_keys(data.temp_email)
        driver.find_element(*Locators.PASSWORD).send_keys(data.password)
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        log_in(driver, data.temp_email)
        order_button_presence = bool(driver.find_elements(*Locators.ORDER_BUTTON))
        driver.quit()
        assert order_button_presence

    def test_register_enter_short_pass_alert(self, driver):
        driver.get(data.stellar_burgers_url)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_ACC_BUTTON))
        driver.find_element(*Locators.LOGIN_ACC_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REG_LINK))
        driver.find_element(*Locators.REG_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REG_BUTTON))
        driver.find_element(*Locators.USER_NAME).send_keys(data.name)
        driver.find_element(*Locators.EMAIL).send_keys(data.temp_email)
        driver.find_element(*Locators.PASSWORD).send_keys('12345')
        driver.find_element(*Locators.REG_BUTTON).click()
        alert_presence = bool(driver.find_elements(By.XPATH, './/p[text()="Некорректный пароль"]'))
        driver.quit()
        assert alert_presence
