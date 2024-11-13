from selenium import webdriver
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.safari.options import Options
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import time

driver = webdriver.Safari()

options = webdriver.SafariOptions()
service = SafariService()
driver = webdriver.Safari(options=options, service=service)

wait_time_imp = 10
driver.implicitly_wait(10)


driver.get('http://demostore.supersqa.com')