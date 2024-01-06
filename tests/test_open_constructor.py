from locators import Locators
from helper import log_in
import data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class TestOpenConstructor:
    def test_open_constructor_acc_menu(self, driver):
        driver.get(f'{data.stellar_burgers_url}/login')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        log_in(driver)
        driver.find_element(*Locators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT_EMAIL))
        driver.find_element(By.XPATH, './/p[text()="Конструктор"]/parent::a').click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.MENU_CONTAINER))
        menu_container_presence = bool(driver.find_elements(*Locators.MENU_CONTAINER))
        driver.quit()
        assert menu_container_presence

    def test_open_constructor_logo_menu(self, driver):
        driver.get(f'{data.stellar_burgers_url}/login')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        log_in(driver)
        driver.find_element(*Locators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT_EMAIL))
        driver.find_element(By.XPATH, './/div[contains(@class, "AppHeader_header__logo")]//a').click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.MENU_CONTAINER))
        menu_container_presence = bool(driver.find_elements(*Locators.MENU_CONTAINER))
        driver.quit()
        assert menu_container_presence
