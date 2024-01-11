from locators import Locators
from data import URLs
from helper import switch_to_tab


class TestConstructor:

    def test_switch_to_buns(self, driver):
        driver.get(URLs.HOMEPAGE)

        switch_to_tab(driver, Locators.BUNS_TAB)
        current_tab = driver.find_element(*Locators.CURRENT_TAB).text

        assert current_tab == 'Булки'

    def test_switch_to_sauces(self, driver):
        driver.get(URLs.HOMEPAGE)

        switch_to_tab(driver, Locators.SAUCE_TAB)
        current_tab = driver.find_element(*Locators.CURRENT_TAB).text

        assert current_tab == 'Соусы'

    def test_switch_to_filling(self, driver):
        driver.get(URLs.HOMEPAGE)

        switch_to_tab(driver, Locators.FILLING_TAB)
        current_tab = driver.find_element(*Locators.CURRENT_TAB).text

        assert current_tab == 'Начинки'
