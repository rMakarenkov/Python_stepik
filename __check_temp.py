from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# create webdriver object
driver = webdriver.Chrome()
driver.implicitly_wait(5)

# get geeksforgeeks.org
driver.get("https://outstaff.bls-soft.ru/")
driver.maximize_window()

# get element
element = driver.find_element(By.CSS_SELECTOR, "#input-85")

# get href attribute
print(element.get_attribute("id"))
driver.quit()
