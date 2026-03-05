from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selene import be, have

# путь к ChromeDriver
service = Service('/Users/max/Documents/chromedriver-mac-x64/chromedriver')

# обычный Chrome
options = webdriver.ChromeOptions()

# инициализация драйвера
browser.config.driver = webdriver.Chrome(service=service, options=options)
browser.config.timeout = 15

# открываем Google
browser.open('https://www.google.com')

# вводим поисковый запрос
browser.element('[name="q"]').should(be.visible).type('QA.GURU').press_enter()

# ждём появления заголовков результатов
results = browser.all('h3')
results.should(have.size_greater_than(0))

# ищем текст среди заголовков
results.element_by(have.text('QA.GURU')).should(be.visible)

print("Тест выполнен ✅ — текст найден")