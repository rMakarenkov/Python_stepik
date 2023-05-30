import pytest
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

url = "https://stepik.org/lesson/236895/step/1"

@pytest.mark.parametrize("url", ["https://stepik.org/lesson/236895/step/1",
                                 "https://stepik.org/lesson/236896/step/1",
                                 "https://stepik.org/lesson/236897/step/1",
                                 "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1",
                                 "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1",
                                 "https://stepik.org/lesson/236905/step/1"])

def test_open_scource(browser, url):
    # прошли авторизацию
    browser.get(f'{url}')
    WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#ember33")))
    browser.find_element(By.CSS_SELECTOR, "#ember33").click()
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys("123")
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys("123")
    browser.find_element(By.CSS_SELECTOR, "#login_form > button").click()
    time.sleep(5)
    answer = math.log(int(time.time()))
    new_answer = str(answer)
    browser.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/article[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/textarea[1]").send_keys(new_answer)
    WebDriverWait(browser, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "[class='submit-submission']")))
    browser.find_element(By.CSS_SELECTOR, "[class='submit-submission']").click()

    time.sleep(2)
    check_message = browser.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/article[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/p[1]")
    assert check_message.text == "Correct!", "Error message"

    time.sleep(5)
