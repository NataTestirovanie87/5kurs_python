from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# Перейдите на сайт
# https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
browser.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Дождитесь загрузки всех картинок.
wait = WebDriverWait(browser, 20)
award_img = wait.until(
    EC.presence_of_element_located((By.ID, "award"))
)

# Получите значение атрибута
src_value = award_img.get_attribute("src")

# Выводим значение в консоль
print(f'Значение атрибута src у картинки: {src_value}')

browser.quit()
