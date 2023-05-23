from selenium import webdriver
import time

driver = webdriver.Chrome()
# driver.execute_script("alert('Robots at work');")
driver.execute_script("document.title='Script executing';alert('Robots at work');")
time.sleep(4)