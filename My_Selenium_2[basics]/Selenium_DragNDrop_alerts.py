from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException
import time

url = 'https://the-internet.herokuapp.com/drag_and_drop'
alerts_url = 'https://demo.automationtesting.in/Alerts.html'
time1 = 1
time2 = 2
time3 = 3
time5 = 5
time10 = 10

driver = webdriver.Chrome()
driver.get(alerts_url)
driver.implicitly_wait(10)

'''
##############################################################################
# drag n drop action start
source_element = driver.find_element(By.XPATH, '//*[@id="column-a"]')
target_element = driver.find_element(By.XPATH, '//*[@id="column-b"]')
time.sleep(3)

actions = ActionChains(driver)

actions.drag_and_drop(source_element, target_element).perform()

# drag n drop action end
##############################################################################
'''
#1st ALERT

#button with alert
Alert_with_OK_btn = driver.find_element(By.CSS_SELECTOR, '#OKTab > button')
Alert_with_OK_btn.click()
# time.sleep(time1)

#alert variable, selenium switch to alert window
Alert_1 = driver.switch_to.alert
# time.sleep(time2)

assert Alert_1.text == 'I am an alert box!', 'Alert text, selenium test, how to work with'
# time.sleep(time1)
Alert_1.accept()
#import pdb; pdb.set_trace()
time.sleep(time3)

#2nd ALERT


Alert_with_OK_CNCL_btn = driver.find_element(By.XPATH,"//a[normalize-space()='Alert with OK & Cancel']")

#moving cursor to button 'Alert with OK & CANCEL'
actions1 = ActionChains(driver)
actions1.move_to_element(Alert_with_OK_CNCL_btn).perform()
Alert_with_OK_CNCL_btn.click()

click_btn_to_cnfrm_box = driver.find_element(By.XPATH,'//*[@id="CancelTab"]/button')
click_btn_to_cnfrm_box.click()


Alert_2 = driver.switch_to.alert
assert Alert_2.text == 'Press a Button !', 'alert znaleziony'
Alert_2.accept()

print('\n\n\nUWAGA!!! Alerty obsłużone prawidłowo!')

time.sleep(time5)



#3rd ALERT


Alert_with_text_box = driver.find_element(By.XPATH,"//a[normalize-space()='Alert with Textbox']")

actions2 = ActionChains(driver)
actions2.move_to_element(Alert_with_text_box).perform()
time.sleep(time3)

Alert_with_text_box.click()
time.sleep(time3)

click_btn_to_prompt = driver.find_element(By.XPATH,'//*[@id="Textbox"]/button')
click_btn_to_prompt.click()

Alert_3 = driver.switch_to.alert
assert Alert_3.text == 'Please enter your name', 'alert znaleziony'
Alert_3.send_keys("                                ")
time.sleep(time3)
Alert_3.send_keys("Skoro to czytasz, to znaczy, ze doszlismy do 3 alertu i gra gitarka")
time.sleep(time3)
Alert_3.accept()

print('\n\nUWAGA!!! Alerty obsłużone prawidłowo!')
time.sleep(time5)

driver.quit()
