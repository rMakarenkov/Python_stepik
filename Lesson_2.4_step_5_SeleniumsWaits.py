import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    driver.get("http://suninjuly.github.io/wait1.html")

    button = driver.find_element(By.ID, "verify")
    button.click()
    message = driver.find_element(By.ID, "verify_message")

    assert "successful" in message.text


finally:
    driver.quit()

