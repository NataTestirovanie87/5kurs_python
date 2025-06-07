from selenium import webdriver
from selenium.webdriver.common.by import By

# инициализация драйвера для Chrome
browser = webdriver.Chrome()


try:
    # переход на нужную по заданию страницу
    browser.get("http://uitestingplayground.com/classattr")

    # Поиск по CSS селектору кнопки и клик по кнопке
    button = browser.find_element(
        By.CSS_SELECTOR, "button.btn.class1.btn-primary.btn-test")
    button.click()
finally:
    # Закрываем браузер
    browser.quit()
