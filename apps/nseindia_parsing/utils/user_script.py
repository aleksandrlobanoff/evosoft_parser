from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def simulate_user_script():
    """
    Симуляция пользовательского сценария использования сайта.
    """
    driver = webdriver.Chrome()
    driver.get("https://www.nseindia.com/")

    # Наводимся на ABOUT
    about = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "ABOUT"))
    )
    ActionChains(driver).move_to_element(about).perform()
    time.sleep(2)

    # Наводимся на INVEST
    invest = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "INVEST"))

    )
    ActionChains(driver).move_to_element(invest).perform()
    time.sleep(2)

    # Наводимся на поле выбора языка
    language = driver.find_element(By.XPATH, '//*[@id="listlanguages"]')
    language.click()
    time.sleep(3)
    language.click()
    time.sleep(3)

    # Скроллим вниз
    scroll_distance = 500  # 500 пикселей для прокрутки
    scroll_repeats = 5  # Количество повторений скроллинга
    script = f"window.scrollBy(0, {scroll_distance});"

    for _ in range(scroll_repeats):
        driver.execute_script(script)
        time.sleep(1)

    time.sleep(5)  # Типа читаем что-то

    scroll_distance = -500  # -500 пикселей для прокрутки
    scroll_repeats = 4  # Количество повторений скроллинга
    script = f"window.scrollBy(0, {scroll_distance});"

    for _ in range(scroll_repeats):
        driver.execute_script(script)
        time.sleep(1)

    time.sleep(5)

    # Кликаем на MOST ACTIVE
    most_active = driver.find_element(By.LINK_TEXT, 'MOST ACTIVE')
    most_active.click()
    time.sleep(3)

    # Действия с полем поиска
    search_input = driver.find_element(By.XPATH, '//*[@id="header-search-input"]')
    ActionChains(driver).move_to_element(search_input).perform() # Наводимся на поле
    search_input.click()  # Нажимаем на поле ввода, чтобы активировать его
    time.sleep(2)
    search_input.send_keys("Gazprom")  # Недоумеваем, почему нет Газпрома? :-)
    time.sleep(3)

    # Очистка текста в поле ввода с помощью комбинации клавиш Ctrl+A и Backspace
    search_input.send_keys(Keys.CONTROL + 'a')
    time.sleep(1)
    search_input.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    search_input.send_keys("UPL")  # Вводим текст "UPL"
    search_input.send_keys(Keys.ENTER)  # Нажимаем клавишу Enter для выполнения поиска
    time.sleep(3)

    # Закрываем драйвер
    driver.quit()
