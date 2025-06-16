from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# Перейдите на сайт http://uitestingplayground.com/textinput.
browser.get("http://uitestingplayground.com/textinput")

# Укажите в поле ввода текст SkyPro.
input_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
input_field.send_keys("SkyPro")

# Нажмите на синюю кнопку.
button = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.ID, "updatingButton"))
)
button.click()

# Получение текста кнопки после изменения
updated_button_text = WebDriverWait(browser, 20).until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)

# Вывод текста кнопки в консоль
button_text = browser.find_element(By.ID, "updatingButton").text
print(f'Текст кнопки: "{button_text}"')

browser.quit()
