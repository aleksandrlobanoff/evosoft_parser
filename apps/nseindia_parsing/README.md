# Парсер данных - это программа, которая собирает данные с веб-страницы и сохраняет их в файл CSV.

## Как работает программа

1. Программа открывает веб-страницу с помощью библиотеки Selenium.
2. При помощи Selenium, программа находит необходимые элементы на странице и извлекает данные из них.
3. Извлеченные данные сохраняются в списки symbol_data и price_data.
4. Затем данные, собранные в списки, записываются в файл CSV с помощью класса CSVWriter.
5. Каждая строка в файле CSV содержит пару значений: имя (symbol) и цена (price).

## Установка и использование

1. Установите необходимые зависимости, выполнив команду:

   pip install -r requirements.txt

2. Запустите программу, выполнив команду:

   python main.py

3. После выполнения программы, файл CSV с данными будет создан.

## Формат файла CSV

Файл CSV содержит два столбца: "Имя" и "Цена". В каждой строке файла CSV содержатся данные о символах и ценах, собранные программой.