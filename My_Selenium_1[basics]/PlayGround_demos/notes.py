from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


web_driver = webdriver.Chrome()
wait_time_imp = 10
web_driver.implicitly_wait(10)

web_driver.get('http://demostore.supersqa.com')
wait_time = 3
time.sleep(wait_time)
#
#
# body = web_driver.find_element(By.TAG_NAME, "body")
# body.send_keys(Keys.PAGE_DOWN)
#
# account_tab = web_driver.find_element(By.LINK_TEXT, 'My account')
# account_tab.click()
# print(f'(type){account_tab}')
# print(f'(type){driver}')
# print(f'(type){wait_time_imp}')
# print(f'(type){wait_time}')






#############################
#############################
#SCROLL UP SCROLL DOWN SCRIPT
#############################
#############################

# # Get the height of the visible part of the browser window
# view_height = web_driver.execute_script("return window.innerHeight;")
#
# # Calculate the target scroll distance to be 3/4 of the visible window height
#  # This determines how much of the page will be scrolled down in total
# scroll_target = int(view_height * 0.75)
#
# # Define the scroll step size by dividing the target scroll distance into 20 smaller steps
# # This allows us to scroll down gradually in smaller increments, creating a smooth scrolling effect
# scroll_step = int(scroll_target / 20)
#
# # Loop to perform smooth scrolling down by 3/4 of the visible page height
# for _ in range(20):  # perform 20 steps to reach the target scroll distance
# # Scroll down by the defined step size in each iteration
#     web_driver.execute_script(f"window.scrollBy(0, {scroll_step});")
#             # Scrolling up
#     scroll_up_step = -scroll_step  # upward scroll step is negative relative to downward
#
# for _ in range(20):  # perform 20 steps to reach the target scroll distance upward
#     web_driver.execute_script(f"window.scrollBy(0, {scroll_up_step});")
#
#
# #end
# input("Press Enter to close the browser...")
# web_driver.quit()