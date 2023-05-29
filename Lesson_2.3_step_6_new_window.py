import time
import math
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/redirect_accept.html")


def calc_x(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    first_window = driver.window_handles[0]
    WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "body > form > "
                                                                                                     "div > div > "
                                                                                                     "button")))
    driver.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    value = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    result = calc_x(value)

    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(f"{result}")
    driver.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()

    allert = driver.switch_to.alert
    print(allert.text)
    allert.accept()

finally:
    time.sleep(2)
    driver.quit()
