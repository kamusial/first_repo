from selenium import webdriver
from selenium4_klasa import LoginPage
from selenium6_funkcja import make_screenshot
import time

def test_login_page():
    driver = webdriver.Chrome()  # opcje?
    page = LoginPage(driver)
    page.open()  #otwieram stronę w przeglądarce
    page.enter_username('standard_user')
    page.enter_password('secret_sauces')
    page.click_login()
    time.sleep(1)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html',make_screenshot(driver)
    driver.quit()

#try, finally driver.quit - sprzątanie po przeglądarce