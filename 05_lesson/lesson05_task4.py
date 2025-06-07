from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем экземпляр драйвера Firefox
driver = webdriver.Firefox()

try:
    # Переходим на нужную по заданию страницу
    driver.get("http://the-internet.herokuapp.com/login")
    wait = WebDriverWait(driver, 5)

    # находим поле для логина и вводим логин
    input_login = driver.find_element(By.CSS_SELECTOR, "input#username")
    input_login.send_keys("tomsmith")

    # находим поле для пароля и вводим пароль
    input_password = driver.find_element(By.CSS_SELECTOR, "input#password")
    input_password.send_keys("SuperSecretPassword!")

    # клик по кнопке входа
    button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    button.click()

    # Ждем появления сообщения об успехе
    success_message = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#flash"))
    )

    # Получаем текст сообщения (убираем лишние пробелы и переносы)
    success_message_text = success_message.text.strip()
    print("Сообщение:", success_message_text)

finally:
    driver.quit()
