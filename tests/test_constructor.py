from locators import Locators
import data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:
    def test_switch_to_buns(self, driver):
        driver.get(data.stellar_burgers_url)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUNS_TAB))
        if driver.find_element(*Locators.CURRENT_TAB).text == "Булки":
            driver.find_element(*Locators.FILLING_TAB).click()
        driver.find_element(*Locators.BUNS_TAB).click()
        WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element(Locators.CURRENT_TAB, "Булки"))
        buns_tab_selected = (driver.find_element(*Locators.CURRENT_TAB).text == "Булки")
        driver.quit()
        assert buns_tab_selected

    def test_switch_to_sauces(self, driver):
        driver.get(data.stellar_burgers_url)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.SAUCE_TAB))
        if driver.find_element(*Locators.CURRENT_TAB).text == "Соусы":
            driver.find_element(*Locators.BUNS_TAB).click()
        driver.find_element(*Locators.SAUCE_TAB).click()
        WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element(Locators.CURRENT_TAB, "Соусы"))
        sauces_tab_selected = (driver.find_element(*Locators.CURRENT_TAB).text == "Соусы")
        driver.quit()
        assert sauces_tab_selected

    def test_switch_to_filling(self, driver):
        driver.get(data.stellar_burgers_url)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.FILLING_TAB))
        if driver.find_element(*Locators.CURRENT_TAB).text == "Начинки":
            driver.find_element(*Locators.SAUCE_TAB).click()
        driver.find_element(*Locators.FILLING_TAB).click()
        WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element(Locators.CURRENT_TAB, "Начинки"))
        filling_tab_selected = (driver.find_element(*Locators.CURRENT_TAB).text == "Начинки")
        driver.quit()
        assert filling_tab_selected
