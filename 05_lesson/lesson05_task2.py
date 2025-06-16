from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()

try:
    # переход на нужную по заданию страницу
    browser.get("http://uitestingplayground.com/dynamicid")

    # клик по кнопке
    button = browser.find_element(
        By.XPATH, "//button[normalize-space(text())='Button with Dynamic ID']")
finally:
    # Закрываем браузер
    browser.quit()
