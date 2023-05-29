import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    driver.get("http://suninjuly.github.io/wait2.html")
    button = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.ID, "verify")))
    button.click()
    message = driver.find_element(By.ID, "verify_message")

    assert "successful" in message.text

    button = WebDriverWait(driver, 5).until_not(ec.element_to_be_clickable((By.ID, "verify")))

finally:
    driver.quit()

