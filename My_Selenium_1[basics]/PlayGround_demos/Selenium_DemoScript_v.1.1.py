from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

#It is useful when working with pages where the loading time of elements may vary.
#f.e. set to 10s, but page will load on 5s, so selenium will wait 5s only.
wait_time_imp = 10
driver.implicitly_wait(10)

#open url
driver.get('http://demostore.supersqa.com')

#==================================
#always wait time set in variable
#time.sleep(5)

wait_time = 1
time.sleep(wait_time)
#==================================

#Scroll down one page (Page Down) *2 simulates a double key press
body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.PAGE_DOWN * 2)
#time.sleep(1)

#Find element by link text - move to second search page
next_search_pg = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/nav/ul/li[3]/a')
next_search_pg.click()

#Select from dropdown list - use Select before (driver.find_element....)
#then variable orderby_list . select_by_ (value , text ...)
orderby_list = Select(driver.find_element(By.CLASS_NAME, 'orderby'))
time.sleep(2)
orderby_list.select_by_value('popularity')
time.sleep(2)

#adding and move to cart
addto_cart_beannie = driver.find_element(By.XPATH, '//*[@id="main"]/ul/li[4]/a[2]')
addto_cart_beannie.click()
time.sleep(2)

view_cart_beannie = driver.find_element(By.XPATH, '//*[@id="main"]/ul/li[4]/a[3]')
view_cart_beannie.click()

time.sleep(5)
#driver.implicitly_wait(10)


# <input type="number" id="quantity_672a0ac453902" class="input-text qty text" step="1" min="0" max="" name="cart[182be0c5cdcd5072bb1864cdee4d3d6e][qty]" value="1" title="Qty" size="4" placeholder="" inputmode="numeric" autocomplete="off">
# <input type="number" id="quantity_672a046d26b2f" class="input-text qty text" step="1" min="0" max="" name="cart[182be0c5cdcd5072bb1864cdee4d3d6e][qty]" value="6" title="Qty" size="4" placeholder="" inputmode="numeric" autocomplete="off">

# Czeka maksymalnie x sekund, aż element będzie obecny w DOM
quantity_cart = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.NAME, "cart[182be0c5cdcd5072bb1864cdee4d3d6e][qty]"))
)
# Utwórz obiekt ActionChains
actions = ActionChains(driver)

# Wykonaj akcję najechania na element
actions.move_to_element(quantity_cart).perform()
quantity_cart.click()


# Teraz możesz od razu operować na tym elemencie
quantity_cart.clear()  # Czyści pole, jeśli jest to pole tekstowe
time.sleep(3)
quantity_cart.send_keys("5")  # Ustawia wartość, np. na 5

time.sleep(2)


# Use arrows keys (sim) to increase & decrease

quantity_cart.send_keys(Keys.ARROW_UP)
time.sleep(1)
quantity_cart.send_keys(Keys.ARROW_UP)
time.sleep(1)
quantity_cart.send_keys(Keys.ARROW_UP)
time.sleep(1)
quantity_cart.send_keys(Keys.ARROW_UP)
time.sleep(1)
quantity_cart.send_keys(Keys.ARROW_UP)
time.sleep(1)
quantity_cart.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
quantity_cart.send_keys(Keys.ARROW_DOWN)
time.sleep(3)

upd_cart_btn = driver.find_element(By.XPATH, '//*[@id="post-7"]/div/div/form/table/tbody/tr[2]/td/button')
upd_cart_btn.click()
time.sleep(4)

flt_rt_rd_btn_3 = driver.find_element(By.ID, 'shipping_method_0_flat_rate2')
flt_rt_rd_btn_3.click()
time.sleep(5)

chng_adrss_link = driver.find_element(By.LINK_TEXT, 'Change address')
chng_adrss_link.click()
time.sleep(3)


country_list = driver.find_element(By.CLASS_NAME, 'select2-selection__rendered')
country_list.click()
time.sleep(2)
country_list_txt = driver.find_element(By.CLASS_NAME, 'select2-search__field')
country_list_txt.click()
time.sleep(2)
country_list_txt.send_keys('Poland')



input("Press Enter to close the browser...")
driver.quit()

# Find the button to increase/decrease the value using XPath and click it
# Increases the value by 5, then Decreases the value by 2
# increase_button = driver.find_element(By.ID, 'quantity_6729fdafaaa89')
# for _ in range(5):
#     increase_button.click()
#
# decrease_button = driver.find_element(By.XPATH, "//button[@class='decrease']")
# for _ in range(2):
#     decrease_button.click()  #

#time.sleep(15)

'''

account_tab = driver.find_element(By.LINK_TEXT, 'My account')
account_tab.click()
time.sleep(3)

#using java script to scroll page up
driver.execute_script('window.scrollBy(0,200);')

#find username field and input name
login = driver.find_element(By.ID, 'username')
login.send_keys('username')

#find password field and input password
password = driver.find_element(By.ID, 'password')
password.send_keys('password')

time.sleep(wait_time)

#select checkbox - "remember me"
login_chbx = driver.find_element(By.NAME,'rememberme')
login_chbx.click()
time.sleep(wait_time)

#press login button
login_button = driver.find_element(By.NAME, 'login')
login_button.click()
time.sleep(wait_time)


# error_list_elem = driver.find_element(By.CLASS_NAME, 'ul.woocommerce-error')
# first_error_elem = error_list_elem[0]
# displayed_error_text = first_error_elem.text
#
# expected_error = 'Error: The username username is not registered on this site. If you are unsure of your username, try your email address instead.'
# assert expected_error == displayed_error_text, 'Displayed error is not expected'
# print('Success')

time.sleep(wait_time * 3)

driver.quit()

'''
