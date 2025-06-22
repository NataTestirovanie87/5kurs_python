import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.test_calculator
def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 60)

    try:
        # Открываем страницу
        driver.get(
            "https:"
            "//bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

        # Вводим значение 45 в поле #delay
        delay_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажимаем кнопку "7"
        button_7 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[.='7']")))
        button_7.click()

        # Нажимаем кнопку "+"
        plus_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[.='+']")))
        plus_button.click()

        # Нажимаем кнопку "8"
        button_8 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[.='8']")))
        button_8.click()

        # Нажимаем "="
        equal_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[.='=']")))
        equal_button.click()

        # Умное ожидание:
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15")
        )

        # Получаем текст результата
        result_element = driver.find_element(By.CSS_SELECTOR, ".screen")
        result_text = result_element.text.strip()

        assert result_text == "15", f"Ожидалось '15', получено '{result_text}'"

    finally:
        driver.quit()
