#from My_Selenium_2[basics].main import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.get('https://magento.softwaretestingboard.com/')
driver.implicitly_wait(10)

# get_attribute href
element = driver.find_element(By.LINK_TEXT, 'Create an Account')
getting_element = element.get_attribute('href')
print('hreff attribiute = ', getting_element)

# get_attribute input - placeholder
element_input = driver.find_element(By.ID, 'search')
getting_element2 = element_input.get_attribute('placeholder')
print('input attribiute = ', getting_element2)

# get_attribute image - src
element_image = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/div/a[1]/img')
getting_element3 = element_image.get_attribute('src')
print('input src image = ', getting_element3)

# get_attribute image - src
element_class = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/div')
getting_element4 = element_class.get_attribute('class')
print('class attribute = ', getting_element4)
time.sleep(6)

#using keys, ENTER, BACKSPACE at search field
element_input.send_keys('Overnight')
time.sleep(2)
element_input.send_keys(Keys.SPACE)
time.sleep(2)
element_input.send_keys('Duddler')
element_input.send_keys(Keys.BACKSPACE)
time.sleep(0.5)
element_input.send_keys(Keys.BACKSPACE)
time.sleep(0.5)
element_input.send_keys(Keys.BACKSPACE)
time.sleep(0.5)
element_input.send_keys(Keys.BACKSPACE)
time.sleep(0.5)
element_input.send_keys(Keys.BACKSPACE)
time.sleep(2)
element_input.send_keys('ffler')
time.sleep(0.5)
element_input.send_keys(Keys.BACKSPACE)
time.sleep(1)
element_input.send_keys(Keys.ENTER)
time.sleep(2)

#select value from dropdown list
dropdown_sortby = driver.find_element(By.XPATH, '//*[@id="sorter"]')
select = Select(dropdown_sortby)
time.sleep(2)
select.select_by_value('price')
time.sleep(1.5)


#moving cursor to element
cursor_on_bag = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[2]/div[2]/ol/li[1]/div/a/span/span/img')
actions = ActionChains(driver)
actions.move_to_element(cursor_on_bag).perform()


# Przykłady atrybutów:
# * href dla linków (<a>),
# * src dla obrazków (<img>),
# * placeholder dla pól tekstowych (<input>),
# * class, id, name, i inne standardowe atrybuty.

time.sleep(10)







driver.quit()