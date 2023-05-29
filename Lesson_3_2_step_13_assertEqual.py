import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestLes1Step11(unittest.TestCase):

    def test_function1(self):
        url1 = "https://suninjuly.github.io/registration1.html"
        driver = webdriver.Chrome()
        driver.get(url1)

        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your phone:']").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your address:']").send_keys("123")

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "body > div > h1"), "Congratulations! You have successfully registered!"))
        var_text_temp = driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(var_text_temp.text, "Congratulations! You have successfully registered!", "Фраза некорректна")

        driver.quit()

    def test_function2(self):
        driver = webdriver.Chrome()
        url2 = "http://suninjuly.github.io/registration2.html"
        driver.get(url2)

        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your name']").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your phone']").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your address']").send_keys("123")

        driver.find_element(By.CSS_SELECTOR, "body > div > form > button").click()
        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "body > div > h1"), "Congratulations! You have successfully registered!"))

        var_text_temp = driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(var_text_temp.text, "Congratulations! You have successfully registered!", "Фраза некорректна")

        driver.quit()
