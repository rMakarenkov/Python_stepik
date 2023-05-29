import time
import math
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/alert_accept.html")

try:
    button = driver.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    button.click()
    confirm = driver.switch_to.alert
    confirm.accept()
    x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    result = str(math.log(abs(12 * math.sin(int(x)))))
    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(result)
    driver.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()
    allert = driver.switch_to.alert.text
    print(allert)

finally:
    time.sleep(2)
    driver.quit()

