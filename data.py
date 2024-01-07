from random import randint

stellar_burgers_url = 'https://stellarburgers.nomoreparties.site'

name = 'Анастасия'
email = 'anastasiyanefedova4042@yandex.ru'
password = '4815162342'

# Генерация email в соответствии с указаниями в задании
temp_email = f'anastasiyanefedova4{randint(100, 999)}@yandex.ru'

# Более приемлемая генерация email
# from time import time
# f'anastasiyanefedova4{int(time())}@yandex.ru'
