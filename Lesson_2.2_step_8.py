import os.path
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/file_input.html"
driver = webdriver.Chrome()

try:
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']").send_keys("Roman")
    driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter last name']").send_keys("Makarenkov")
    driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter email']").send_keys("romgover@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "File.txt")
    driver.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(5)
    driver.quit()
