from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/get_attribute.html")

try:
    x = driver.find_element(By.CSS_SELECTOR, "#treasure")
    x_atr = x.get_attribute("valuex")
    print(x_atr)
    result = calc(x_atr)

    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(result)
    driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(5)
    driver.quit()
