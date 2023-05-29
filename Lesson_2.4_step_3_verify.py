import time
import os
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/wait1.html")

try:
    button = driver.find_element(By.ID, "verify")
    button.click()
    message = driver.find_element(By.ID, "verify_message")

    assert "successful!" in message.text

finally:
    time.sleep(2)
    driver.quit()
