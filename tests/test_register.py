from locators import Locators
from helper import log_in, wait_until_visible
import data
from selenium.webdriver.common.by import By


class TestRegister:

    def test_register_enter_valid_creds(self, driver):
        driver.get(data.stellar_burgers_url)

        wait_until_visible(driver, Locators.LOGIN_ACC_BUTTON)
        driver.find_element(*Locators.LOGIN_ACC_BUTTON).click()

        wait_until_visible(driver, Locators.REG_LINK)
        driver.find_element(*Locators.REG_LINK).click()

        wait_until_visible(driver, Locators.REG_BUTTON)
        driver.find_element(*Locators.USER_NAME).send_keys(data.name)
        driver.find_element(*Locators.EMAIL).send_keys(data.temp_email)
        driver.find_element(*Locators.PASSWORD).send_keys(data.password)
        driver.find_element(*Locators.REG_BUTTON).click()

        log_in(driver, data.temp_email)
        wait_until_visible(driver, Locators.ORDER_BUTTON, 'Не удалось авторизоваться после регистрации')

        driver.quit()

    def test_register_enter_short_pass_alert(self, driver):
        driver.get(data.stellar_burgers_url)

        wait_until_visible(driver, Locators.LOGIN_ACC_BUTTON)
        driver.find_element(*Locators.LOGIN_ACC_BUTTON).click()

        wait_until_visible(driver, Locators.REG_LINK)
        driver.find_element(*Locators.REG_LINK).click()

        wait_until_visible(driver, Locators.REG_BUTTON)
        driver.find_element(*Locators.USER_NAME).send_keys(data.name)
        driver.find_element(*Locators.EMAIL).send_keys(data.temp_email)
        driver.find_element(*Locators.PASSWORD).send_keys('12345')
        driver.find_element(*Locators.REG_BUTTON).click()

        alert_presence = bool(driver.find_elements(By.XPATH, './/p[text()="Некорректный пароль"]'))
        driver.quit()
        assert alert_presence, 'Не найдено уведомление "Некорректный пароль"'
