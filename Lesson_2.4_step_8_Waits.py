import os
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc_x(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

driver = webdriver.Chrome()

try:
    driver.get("https://suninjuly.github.io/explicit_wait2.html")
    first_window = driver.window_handles[0]
    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
    button = driver.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    check = driver.find_element(By.XPATH, "//*[@id='simple_text']")

    assert "Math is real magic!" in check.text

    value = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(f'{calc_x(value)}')
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#solve")))

    driver.find_element(By.CSS_SELECTOR, "#solve").click()

    allert = driver.switch_to.alert
    print(allert.text)

finally:
    time.sleep(5)
    driver.quit()
