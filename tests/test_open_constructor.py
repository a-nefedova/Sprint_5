from locators import Locators
from helper import log_in, wait_until_visible
import data
from selenium.webdriver.common.by import By


class TestOpenConstructor:

    def test_open_constructor_acc_menu(self, driver):
        driver.get(URLs.LOGIN)

        log_in(driver)
        wait_until_visible(driver, Locators.ORDER_BUTTON)

        driver.find_element(*Locators.ACCOUNT_LINK).click()
        wait_until_visible(driver, Locators.ACCOUNT_EMAIL)

        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        wait_until_visible(driver, Locators.MENU_CONTAINER, 'Не удалось найти секцию с ингредиентами')

        driver.quit()

    def test_open_constructor_logo_menu(self, driver):
        driver.get(URLs.LOGIN)

        log_in(driver)
        wait_until_visible(driver, Locators.ORDER_BUTTON)

        driver.find_element(*Locators.ACCOUNT_LINK).click()
        wait_until_visible(driver, Locators.ACCOUNT_EMAIL)

        driver.find_element(*Locators.HEADER_LOGO).click()
        wait_until_visible(driver, Locators.MENU_CONTAINER, 'Не удалось найти секцию с ингредиентами')

        driver.quit()
