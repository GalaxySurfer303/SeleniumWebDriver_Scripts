from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://magento.softwaretestingboard.com/')
driver.implicitly_wait(10)
driver.quit()
