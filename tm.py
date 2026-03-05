from selene.support.shared import browser
from selene import have, be
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# ChromeDriver
service = Service('/Users/max/Documents/chromedriver-mac-x64/chromedriver')
options = webdriver.ChromeOptions()
browser.config.driver = webdriver.Chrome(service=service, options=options)
browser.config.timeout = 20

# открываем сайт напрямую
browser.open('https://lemanapro.ru')
time.sleep(5)  # ждём подгрузки контента

# выбираем заголовки по реальному селектору
results = browser.all('h3')  # здесь может быть другой селектор
results.should(have.size_greater_than(0))

# ищем конкретный текст
results.element_by(have.text('Предложение месяца')).should(be.visible).click()

print("✅ Тест выполнен — текст найден")