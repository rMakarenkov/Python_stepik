from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/math.html")

x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
y = calc(x)
driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
driver.find_element(By.CSS_SELECTOR, "body > div > form > button").click()

time.sleep(5)
driver.quit()

