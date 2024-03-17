from selenium import webdriver


class DataScraper:
    def __init__(self) -> None:
        """Инициализация класса"""
        self.symbol_data: list[str] = []  # Создаем пустой список symbol_data для хранения символов
        self.price_data: list[float] = []  # Создаем пустой список price_data для хранения цен
        self.driver: webdriver.Chrome = webdriver.Chrome()  # Инициализируем драйвер Selenium и используем Chrome
