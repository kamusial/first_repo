from selenium import webdriver
from selenium4_klasa import LoginPage
from selenium6_funkcja import make_screenshot
import time
import pytest
from selenium.common.exceptions import TimeoutException

test_data = [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html')
]

@pytest.mark.parametrize('username, password, url', test_data)
def test_login_page(username, password, url):
    driver = webdriver.Chrome()  # opcje?
    page = LoginPage(driver)
    page.open()  #otwieram stronę w przeglądarce
    page.enter_username(username)
    page.enter_password(password)
    page.click_login()
    time.sleep(1)
    try:
        assert driver.current_url == url, make_screenshot(driver)
    finally:
        driver.quit()

