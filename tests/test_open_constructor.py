from locators import Locators
from helper import log_in_and_get_to_acc, wait_until_visible
from data import URLs


class TestOpenConstructor:

    def test_open_constructor_button(self, driver):
        driver.get(URLs.LOGIN)

        log_in_and_get_to_acc(driver)

        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        constructor_header = wait_until_visible(driver, Locators.H1_HEADER).text

        assert constructor_header == "Соберите бургер"

    def test_open_constructor_logo(self, driver):
        driver.get(URLs.LOGIN)

        log_in_and_get_to_acc(driver)

        driver.find_element(*Locators.LOGO).click()

        constructor_header = wait_until_visible(driver, Locators.H1_HEADER).text

        assert constructor_header == "Соберите бургер"
