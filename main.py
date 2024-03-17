import time

from utils.csvwriter import CSVWriter
from utils.datascraper import DataScraper


def main():
    """
    Основная функция программы.
    """
    writer = CSVWriter('data.csv')  # Создаем объект для записи в файл CSV
    max_retries = 5  # Максимальное количество попыток

    while max_retries > 0:  # Пока есть попытки
        try:
            scraper = DataScraper()  # Создаем новый объект Scraper на каждой итерации

            scraper.scrape_data()  # Выполняем парсинг данных

            if scraper.symbol_data and scraper.price_data:  # Если есть данные для записи
                writer.write_to_csv(scraper.symbol_data, scraper.price_data)  # Записываем данные в файл CSV
                print("Операция завершена успешно")
                break  # Прекращаем выполнение цикла
            else:
                print("Запрашиваемые данные не найдены на странице. Повторная попытка...")
                max_retries -= 1  # Уменьшаем количество попыток

            print("Попыток осталось:", max_retries)
            time.sleep(2)  # Пауза в 2 секунды перед следующей попыткой

        except Exception as e:
            print("Произошла ошибка:", str(e))
            max_retries -= 1  # Уменьшаем количество попыток в случае ошибки

    if max_retries == 0:
        print("Все попытки закончились. Операция не выполнена")


if __name__ == "__main__":
    main()
