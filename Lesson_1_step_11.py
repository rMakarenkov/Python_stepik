from selenium import webdriver
from selenium.webdriver.common.by import By

import time

try:
    url = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(url)

    """Код, который заполняет обязательные поля"""
    input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your name']")
    input1.send_keys("Roman Makarenkov")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
    input2.send_keys("romgover@gmail.com")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your phone']")
    input3.send_keys("123 123 123")
    input4 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your address']")
    input4.send_keys("321 321 321")

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

