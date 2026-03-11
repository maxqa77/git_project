import os
import pytest
from selene import browser, be, have
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Настройка Firefox через webdriver_manager с использованием Service
@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    # Устанавливаем driver для Selene
    browser.config.driver = driver

    # Открываем локальный файл
    url = "file://" + os.path.abspath("login.html")
    browser.open(url)

    yield  # Позволяет тестам работать с браузером

    browser.quit()  # Закрытие браузера после выполнения тестов

def test_successful_login(setup_browser):
    # Взаимодействие с элементами страницы для успешного логина
    browser.element('[id="username"]').type('admin')
    browser.element('[id="password"]').type('admin1')
    browser.element('[type="submit"]').click()

    # Проверка успешного входа (например, наличие сообщения о успешной авторизации)
    browser.element('[id="message"]').should(have.text('Ты вошёл пидр!'))

def test_unsuccessful_login(setup_browser):
    # Взаимодействие с элементами страницы для неуспешного логина
    browser.element('[id="username"]').type('wrong_user')
    browser.element('[id="password"]').type('wrong_password')
    browser.element('[type="submit"]').click()

    # Проверка неуспешного входа (например, наличие сообщения о неправильном логине или пароле)
    browser.element('[id="message"]').should(have.text('Запрет пидр!.'))

def test_empty_username(setup_browser):
    # Взаимодействие с элементами страницы для пустого логина
    browser.element('[id="username"]').type('')  # Пустой логин
    browser.element('[id="password"]').type('admin1')
    browser.element('[type="submit"]').click()

    # Проверка наличия сообщения о пустом логине
    browser.element('[id="message"]').should(have.text('Долбоёб где имя?'))

def test_empty_password(setup_browser):
    # Взаимодействие с элементами страницы для пустого пароля
    browser.element('[id="username"]').type('admin')
    browser.element('[id="password"]').type('')  # Пустой пароль
    browser.element('[type="submit"]').click()

    # Проверка наличия сообщения о пустом пароле
    browser.element('[id="message"]').should(have.text('Пароль введи урод!'))