from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

# ожидание 10 сек
browser.implicitly_wait(10)

# Перейдите на страницу http://uitestingplayground.com/ajax.
browser.get("https://uitestingplayground.com/ajax")

# Нажмите на синюю кнопку.
browser.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Нажмите кнопку ниже и дождитесь появления данных (15 секунд)
# Получите текст из зеленой плашки
wait = WebDriverWait(browser, 15)
content = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#content p.bg-success"))
)

# Выведите его в консоль ("Data loaded with AJAX get request.")
wait = WebDriverWait(browser, 10)
txt_element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#content p.bg-success"))
)
txt = txt_element.text
print(f'Текст плашки: "{txt}"')

browser.quit()
