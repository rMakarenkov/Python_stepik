import time

from variable_stepik import Variable

""" webdriver это и есть набор команд для управления браузером """
from selenium import webdriver

""" импортируем класс By, который позволяет выбрать способ поиска элемента """
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(2)

""" Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке """
driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(2)

""" Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
Ищем поле для ввода текста """
textarea = driver.find_element(By.CSS_SELECTOR, Variable.INPUT)

""" Напишем текст ответа в поле """
textarea.send_keys("123 321 123 321")
time.sleep(2)
textarea.clear()
textarea.send_keys("123 11111111111111111111")
time.sleep(2)

submit_button = driver.find_element(By.XPATH, Variable.BUTTON_SUBMIT)
submit_button.click()
time.sleep(2)

driver.quit()
