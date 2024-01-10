from locators import Locators
from data import URLs
from helper import wait_until_visible


def switch_to_tab(driver, tab_locator):
    driver.get(URLs.HOMEPAGE)

    wait_until_visible(driver, tab_locator)
    if driver.find_element(*Locators.CURRENT_TAB).text == driver.find_element(*tab_locator).text:
        driver.find_element(*Locators.UNSELECTED_TAB).click()
    driver.find_element(*tab_locator).click()

    tab_name_selected = (driver.find_element(*Locators.CURRENT_TAB).text == driver.find_element(*tab_locator).text)
    driver.quit()

    return tab_name_selected


class TestConstructor:

    def test_switch_to_buns(self, driver):
        assert switch_to_tab(driver, Locators.BUNS_TAB), 'Не удалось перейти на вкладку "Булки"'

    def test_switch_to_sauces(self, driver):
        assert switch_to_tab(driver, Locators.SAUCE_TAB), 'Не удалось перейти на вкладку "Соусы"'

    def test_switch_to_filling(self, driver):
        assert switch_to_tab(driver, Locators.FILLING_TAB), 'Не удалось перейти на вкладку "Начинки"'
