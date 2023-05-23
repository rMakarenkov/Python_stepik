from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/selects1.html") #https://suninjuly.github.io/selects2.html

try:
    value1 = driver.find_element(By.CSS_SELECTOR, "#num1").text
    print(value1)
    value2 = driver.find_element(By.CSS_SELECTOR, "#num2").text
    print(value2)
    finnaly_value = int(value1) + int(value2)
    print(finnaly_value)

    # select = Select(driver.find_element(By.CSS_SELECTOR, "#dropdown")) - второй способ решения задачи
    # select.select_by_visible_text(str(finnaly_value)) - второй способ решения задачи

    driver.find_element(By.CSS_SELECTOR, "#dropdown").click()
    driver.find_element(By.CSS_SELECTOR, f"[value='{finnaly_value}']").click()
    driver.find_element(By.CSS_SELECTOR, "body > div > form > button").click()

finally:
    time.sleep(5)
    driver.quit()
