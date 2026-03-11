import os
from selene import browser, be, have
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Настройка Firefox через webdriver_manager с использованием Service
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# Устанавливаем driver для Selene
browser.config.driver = driver

# Открываем локальный файл
url = "file://" + os.path.abspath("login.html")
browser.open(url)

# Взаимодействие с элементами страницы
browser.element('[id="username"]').type('admin')
browser.element('[id="password"]').type('admin1')
browser.element('[type="submit"]').click()

browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))