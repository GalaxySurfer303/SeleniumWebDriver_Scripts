from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException
import time

windows_url = 'https://demo.automationtesting.in/Windows.html'
frames_url = 'https://demo.automationtesting.in/Frames.html'
sc_url = 'https://soundcloud.com/discover'
bc_url = 'https://galaxysurfer303.bandcamp.com/dashboard'
time1 = 1
time2 = 2
time3 = 3
time5 = 5
time10 = 10

driver = webdriver.Chrome()
driver.get(frames_url)
driver.implicitly_wait(10)

