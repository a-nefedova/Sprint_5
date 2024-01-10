from random import randint


class URLs:

    HOMEPAGE = 'https://stellarburgers.nomoreparties.site'
    LOGIN = f'{HOMEPAGE}/login'
    REGISTER = f'{HOMEPAGE}/register'
    ACCOUNT = f'{HOMEPAGE}/account/profile'
    FORGOT_PASS = f'{HOMEPAGE}/forgot-password'


class Creds:

    name = 'Анастасия'
    email = 'anastasiyanefedova4042@yandex.ru'
    password = '4815162342'

    temp_email = f'anastasiyanefedova4{randint(100, 999)}@yandex.ru'
