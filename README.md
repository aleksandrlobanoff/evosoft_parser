## Описание проекта
Этот проект состоит из двух приложений, которые выполняют парсинг данных с веб-страницы и получение последних твитов Илона Маска.

## Задача
Основная задача первого приложения - собрать данные с веб-страницы https://www.nseindia.com/ и сохранить их в файл CSV. Второе приложение выполняет парсинг последних твитов Илона Маска с использованием HTTP-запросов и выводит результат в лог-файл.

## Решение
Первое приложение использует библиотеку Selenium для открытия веб-страницы, нахождения элементов и извлечения данных. Данные сохраняются в файл CSV при помощи класса CSVWriter. Также в приложении реализован пользовательский сценарий использования сайта, направленный на имитацию действий пользователя.

Второе приложение использует HTTP-запросы для получения последних твитов Илона Маска и выводит текст твитов в лог-файл. Также выводятся ссылки на аккаунты авторов последних 3 комментариев.

---

Ссылки на README.md файлы каждого проекта:

1. [README.md для первого проекта](apps/nseindia_parsing/README.md)
2. [README.md для второго проекта](apps/ElonMask/README.md)