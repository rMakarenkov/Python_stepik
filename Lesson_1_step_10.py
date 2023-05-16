from selenium import webdriver
from selenium.webdriver.common.by import By

import time

try:
    url = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(url)

    """Код, который заполняет обязательные поля"""
    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    input1.send_keys("Roman")
    input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    input2.send_keys("Makarnekov")
    input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    input3.send_keys("romgover@gmail.com")

    """Нажимаем кнопку и отправляем заполненную форму"""
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    """Ждем, чтобы подгрузился элемент"""
    time.sleep(1)

    """Осуществляется переход на другую страницу, ищем элемент срдержаший текст через By.TAG_NAME"""
    ver_text = browser.find_element(By.TAG_NAME, "h1")
    assert "Congratulations! You have successfully registered!" == ver_text.text
    print("Тест успешно выполнен!")

finally:
    time.sleep(5)
    browser.quit()

