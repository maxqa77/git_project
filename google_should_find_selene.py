from selene.support.shared import browser
from selene import have, be
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# путь к ChromeDriver
service = Service('/Users/max/Documents/chromedriver-mac-x64/chromedriver')
options = webdriver.ChromeOptions()

browser.config.driver = webdriver.Chrome(service=service, options=options)
browser.config.timeout = 20

# открываем Google
browser.open('https://www.google.com/webhp?igu=1')

# поиск
browser.element('[name="q"]').should(be.visible).type('лемана про').press_enter()

# ждём появления заголовков
results = browser.all('h3')
results.should(have.size_greater_than(0))

# выбираем результат по части текста через lambda
results.element_by(lambda e: 'lemanapro.ru' in e.text).click()

# ждём загрузки страницы
time.sleep(2)

# проверка заголовка на странице
browser.all('h3').element_by(lambda e: 'Предложение месяца' in e.text).should(be.visible)