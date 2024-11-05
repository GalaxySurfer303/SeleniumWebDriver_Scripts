from webbrowser import Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time



#headless mode (test without opening browser)
options = Options()
options.add_argument('--headless=new')
# another option to do that - options.headless = True

driver=webdriver.Chrome(options=options)
#open browser
driver.get("https://www.python.org")
search_input = driver.find_element(By.NAME, 'q')


time.sleep(3)

#search field + button
search_input.send_keys('selenium')
search_btt = driver.find_element(By.CLASS_NAME, 'search-button')
search_btt.click()


print(f'\nSearch input = {search_input},\nSearch button CLASS NAME = {search_btt}')  #shows elements ID's

time.sleep(10)  #wait 10 sec before close browser







'''
driver.get('https://www.python.org')

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
# ...
driver.quit()
'''

'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
'''