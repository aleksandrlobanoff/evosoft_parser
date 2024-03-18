from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


def setup_logger():
    # Настройка логирования в файл
    logging.basicConfig(format='%(asctime)s - %(message)s', filename='tweets.log', level=logging.INFO)


def rss_app(browser, url):
    # Обращаемся к сервису rss.app

    # GET - запрос на страницу поиска по ссылке
    browser.get('https://rss.app/rss-feed/create-twitter-rss-feed')

    # Наводимся на input
    inpt = browser.find_element(By.ID, ':r0:')
    # Вставляем в input ссылку на страницу Илона
    inpt.send_keys(url)

    button_accept = browser.find_element(By.ID, 'provider-submit').click()

    # Явное ожидание загрузки элементов на странице
    feed = WebDriverWait(browser, timeout=120).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'tss-k2zsea-FeedCardOverview-content'))
    )

    # Возвращаем browser для дальнейшей работы с этой страницей
    return browser
