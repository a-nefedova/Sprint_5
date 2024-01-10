import data
from selenium.webdriver.common.by import By


class Locators:

    USER_NAME = (By.XPATH, './/form//label[text()="Имя"]/parent::*/input')  # поле для ввода имени при регистрации
    EMAIL = (By.XPATH, './/form//label[text()="Email"]/parent::*/input')    # поле для ввода email при регистрации
    PASSWORD = (By.XPATH, './/input[@type="password"]')                 # поле для ввода пароля при регистрации

    LOGIN_ACC_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')    # кнопка "Войти в аккаунт" на главной
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')                  # кнопка "Войти" в форме логина
    LOGIN_LINK = (By.XPATH, './/a[@href="/login"]')     # ссылка "Войти" в формах регистрации и восстановления пароля

    REG_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')  # кнопка "Зарегистрироваться" в форме регистрации
    REG_LINK = (By.XPATH, './/a[@href="/register"]')                   # ссылка "Зарегистрироваться" в форме логина

    ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')    # кнопка "Оформить заказ"

    ACCOUNT_LINK = (By.XPATH, './/a[@href="/account"]')                # ссылка на Личный кабинет
    ACCOUNT_EMAIL = (By.XPATH,                                         # поле с тестовым email в Личном кабинете
                     f'.//label[text()="Логин"]/parent::div/input[@value]')

    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]')                                 # кнопка "Выход"

    HEADER_LOGO = (By.XPATH, './/div[contains(@class, "AppHeader_header__logo")]//a')       # логотип сервиса
    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text()="Конструктор"]/parent::a')                   # ссылка на Конструктор

    MENU_CONTAINER = (By.XPATH, './/div[contains(@class, "menuContainer")]')                # секция с ингредиентами
    BUNS_TAB = (By.XPATH, './/div[contains(@class, "noselect")]/*[text()="Булки"]')         # вкладка "Булки"
    SAUCE_TAB = (By.XPATH, './/div[contains(@class, "noselect")]/*[text()="Соусы"]')        # вкладка "Соусы"
    FILLING_TAB = (By.XPATH, './/div[contains(@class, "noselect")]/*[text()="Начинки"]')    # вкладка "Начинки"
    CURRENT_TAB = (By.XPATH, './/div[contains(@class, "current")]/*')                       # текущая вкладка
    UNSELECTED_TAB = (By.XPATH,                                                             # неактивная вкладка
                      './/div[not(contains(@class, "current")) and contains(@class, "noselect")]/*')
