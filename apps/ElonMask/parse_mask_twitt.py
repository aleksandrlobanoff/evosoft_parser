from selenium.webdriver import Chrome, ChromeOptions
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
def main(browser):
    # Функция для работы со страницей постов Илона
    posts = []
    # Делаем scroll на странице, пока нам не будут доступны минимум 10 постов
    while len(posts) < 10:
        # Делаем Scroll
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Обновляем список постов
        posts = browser.find_elements(By.XPATH, '//a[@class="MuiTypography-root MuiTypography-h3 tss-1h8hsy-FeedCardOverview-title mui-1ti1707-Typography-fontWeightBold"]')

    # Обход 10 последних постов и сохранение текста в лог-файл
    for num, post in enumerate(posts[:10], 1):
        text = post.text
        logging.info(f'Пост #{num}:\n\t{text if text else "Текст отсутствует"}\n')

        # Получаем ссылки на аккаунты авторов последних 3 комментариев
        comments = post.find_elements(By.XPATH, './/div[contains(@class, "tss-0emlzn-Comment-content")]')
        author_links = [comment.find_element(By.XPATH, './a').get_attribute('href') for comment in comments[-3:]]

        # Выводим ссылки на аккаунты авторов комментариев в лог
        for link in author_links:
            logging.info(f'\tСсылка на автора комментария: {link}\n')


if __name__ == '__main__':
    setup_logger()
    options = ChromeOptions()

    options.add_argument("--disable-gpu")

    with Chrome(options=options) as browser:
        user_url = 'https://twitter.com/elonmusk'
        new_browser = rss_app(browser, user_url)
        main(browser)