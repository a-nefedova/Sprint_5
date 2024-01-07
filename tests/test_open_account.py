from locators import Locators
from helper import log_in, wait_until_visible
import data


class TestOpenAccount:

    def test_open_account_creds(self, driver):
        driver.get(f'{data.stellar_burgers_url}/login')

        log_in(driver)
        wait_until_visible(driver, Locators.ORDER_BUTTON)

        driver.find_element(*Locators.ACCOUNT_LINK).click()

        wait_until_visible(driver, Locators.ACCOUNT_EMAIL, 'Не удалось найти учётные данные аккаунта')

        driver.quit()
