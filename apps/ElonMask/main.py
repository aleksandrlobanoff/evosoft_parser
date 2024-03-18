from selenium.webdriver.common.by import By
import logging
from selenium.webdriver import Chrome, ChromeOptions
from apps.ElonMask.utils import setup_logger, rss_app


def main(browser):
    # Функция для работы со страницей постов Илона
    posts = []
    # Делаем scroll на странице, пока нам не будут доступны минимум 10 постов
    while len(posts) < 10:
        # Делаем Scroll
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Обновляем список постов
        posts = browser.find_elements(By.XPATH,
                                      '//a[@class="MuiTypography-root MuiTypography-h3 tss-1h8hsy-FeedCardOverview-title mui-1ti1707-Typography-fontWeightBold"]')

    # Обход 10 последних постов и сохранение текста в лог-файл
    for num, post in enumerate(posts[:10], 1):
        text = post.text
        # Логирование текста поста
        logging.info(f'Пост #{num}:\n\t{text if text else "Текст отсутствует"}\n')

        # Получаем ссылки на аккаунты авторов последних 3 комментариев
        comments = post.find_elements(By.XPATH, './/div[contains(@class, "tss-0emlzn-Comment-content")]')
        author_links = [comment.find_element(By.XPATH, './a').get_attribute('href') for comment in comments[-3:]]

        # Логирование ссылок на аккаунты авторов комментариев
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
