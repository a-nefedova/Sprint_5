from locators import Locators
from helper import log_in, wait_until_visible
import data


class TestLogout:

    def test_logout_login_button(self, driver):
        driver.get(f'{data.stellar_burgers_url}/login')

        log_in(driver)
        wait_until_visible(driver, Locators.ORDER_BUTTON)

        driver.find_element(*Locators.ACCOUNT_LINK).click()
        wait_until_visible(driver, Locators.ACCOUNT_EMAIL)

        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        wait_until_visible(driver, Locators.LOGIN_BUTTON, 'Не удалось найти форму авторизации')

        driver.quit()
