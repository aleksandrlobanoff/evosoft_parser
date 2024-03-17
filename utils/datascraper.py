from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains
import time

from selenium.webdriver.support.wait import WebDriverWait


class DataScraper:
    def __init__(self) -> None:
        """Инициализация класса"""
        self.symbol_data: list[str] = []  # Создаем пустой список symbol_data для хранения символов
        self.price_data: list[str] = []  # Создаем пустой список price_data для хранения цен
        self.driver: webdriver.Chrome = webdriver.Chrome()  # Инициализируем драйвер Selenium и используем Chrome

    def scrape_data(self):

        self.driver.get("https://www.nseindia.com/")
        # Наводимся на "MARKET DATA"
        # Ожидаем загрузку элемента "MARKET DATA"
        market_data = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "MARKET DATA"))
        )
        ActionChains(self.driver).move_to_element(market_data).perform()  # Наводимся на MARKET DATA

        # Ожидаем, пока элемент "Pre-Open Market" станет видимым
        pre_open_market = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Pre-Open Market"))
        )
        ActionChains(self.driver).move_to_element(pre_open_market).perform()  # Наводимся на pre_open_market
        time.sleep(1)
        pre_open_market.click()  # Кликаем на pre_open_market

        # Ожидание загрузки страницы "Pre-Open Market"
        self.driver.implicitly_wait(5)

        # Находим все элементы с классом "symbol-word-break"
        symbol_elements = self.driver.find_elements(By.CLASS_NAME, "symbol-word-break")
        # Находим все элементы с классом "bold.text-right"
        price_elements = self.driver.find_elements(By.CLASS_NAME, "bold.text-right")

        # Заполнение данных символов
        for i in range(len(symbol_elements)):
            symbol_text = symbol_elements[i].text
            self.symbol_data.append(symbol_text)

        # Заполнение данных цен
        for i in range(len(price_elements)):
            price_text = price_elements[i].text
            if price_text != 'FINAL':  # Исключаем появление названия столбца "FINAL" в данных
                self.price_data.append(price_text)

        # Завершение работы драйвера
        self.driver.quit()
