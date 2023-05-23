import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://SunInJuly.github.io/execute_script.html"
driver = webdriver.Chrome()
driver.get(link)

try:
    valueX = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    result = calc(valueX)
    driver.execute_script("window.scrollBy(0, 100);")
    answer = driver.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(str(result))
    driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(5)
    driver.quit()
