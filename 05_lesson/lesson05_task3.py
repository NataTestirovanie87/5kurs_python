from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создаем экземпляр драйвера Firefox
driver = webdriver.Firefox()

try:
    # Переходим на нужную по заданию страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Находим поле ввода
    input_field = driver.find_element(By.XPATH, "//input[@type='number']")
    time.sleep(3)  # задержка для наглядности

    # Вводим текст "Sky"
    input_field.send_keys("Sky")
    time.sleep(3)  # задержка для наглядности

    # Очищаем поле
    input_field.clear()
    time.sleep(3)

    # Вводим текст "Pro"
    input_field.send_keys("Pro")
    time.sleep(3)

finally:
    # Закрываем браузер
    driver.quit()
