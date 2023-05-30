import pytest
from selenium.webdriver.common.by import By


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link_two(browser, language):
    link2 = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link2)
    browser.find_element(By.CSS_SELECTOR, "#login_link")