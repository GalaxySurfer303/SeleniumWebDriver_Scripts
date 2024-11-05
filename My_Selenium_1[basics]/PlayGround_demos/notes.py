from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
wait_time_imp = 10
driver.implicitly_wait(10)

driver.get('http://demostore.supersqa.com')
wait_time = 3
time.sleep(wait_time)


body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.PAGE_DOWN)

account_tab = driver.find_element(By.LINK_TEXT, 'My account')
account_tab.click()
print(f'(type){account_tab}')
print(f'(type){driver}')
print(f'(type){wait_time_imp}')
print(f'(type){wait_time}')



driver.quit()