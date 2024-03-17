import csv


class CSVWriter:
    def __init__(self, filename):
        """
        Инициализация класса CSVWriter.
        :param filename: Имя файла CSV для записи данных.
        """
        self.filename = filename

    def write_to_csv(self, name, price):
        """
        Запись данных в файл CSV.
        :param name: Список с именами.
        :param price: Список с ценами.
        """
        try:
            with open(self.filename, "w", newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["Имя", "Цена"])

                for i in range(len(name)):
                    symbol_text = name[i]
                    price_text = price[i]
                    csv_writer.writerow([symbol_text, price_text])
        except Exception as e:
            print("Ошибка при записи данных в файл CSV:", str(e))
