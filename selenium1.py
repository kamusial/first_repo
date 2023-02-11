from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://google.com')
print('Nazwa strony ',driver.title)
button1_accept = driver.find_element('id', 'L2AGLb')
button1_accept.click()
#print(button1_accept)
pole_szukaj = driver.find_element('name', 'q')
pole_szukaj.send_keys('Czy jutro jest niedziela handlowa')
przycisk_szukaj = driver.find_element('name','btnK')
przycisk_szukaj.submit()
time.sleep(2)
driver.quit()

