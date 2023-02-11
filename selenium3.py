from selenium import webdriver
from selenium.webdriver.common.by import By  #pomoc w lokalizacji elementów
from selenium.webdriver.support.wait import WebDriverWait   #klasa oczekiwator
from selenium.webdriver.support import expected_conditions as excon  #umożliwia sprawdzenie warunku
import time
from selenium.common.exceptions import TimeoutException

def czekaj_na_id(element_id):
    timeout = 10
    timeout_message = f"Element o id '{element_id}' nie pojawił się w czasie {timeout} s. "
    lokalizator = (By.ID, element_id)   # szukanie po ID i konkretnej wartości
    znaleziono = excon.visibility_of_element_located(lokalizator)  #patyk do dźgania strony
    #obiekt będzie pytany, czy jest OK, a odpowiedź zależy od tego, czy element szukany po lokalizatorze jest widoczny
    oczekiwator = WebDriverWait(driver, timeout)  #driver czeka max timeout
    return oczekiwator.until(znaleziono, timeout_message)  #czekamy, aż znajdzie, until odpytuje do timeout

driver = webdriver.Chrome()
driver.get('http://www.saucedemo.com')
try:
    login_button = czekaj_na_id('login-button')
except TimeoutException:
    print('Nie znaleziono')
#    raise
else:
    print('Znaleziono')
    print(login_button)
finally:
    time.sleep(5)
    driver.quit()