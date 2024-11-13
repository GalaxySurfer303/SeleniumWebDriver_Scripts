import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

#from PlayGround_demos.notes import web_driver

#from selenium.webdriver.chrome.service import Service as Chrome_Service

#from PlayGround_demos.notes import driver

# motherfuckers = 'motherfuckers'
# fucking = 'fucking'
# print('hello %s , can you feel the %s bass' % (motherfuckers, fucking))


########################################################################
# test in the class form
base_url = 'https://magento.softwaretestingboard.com/'
username = 'mr. Galaxy'
surname = 'Surfer'
password = 'Jestemzdrowy1'
user_email = 'galaxy.surfer@email.com'

class CreateAccount():

    def __init__(self):
        self.web_driver = webdriver.Chrome()
        self.web_driver.delete_all_cookies()  #delete cookies before tests
        self.web_driver.get(base_url)
        print(self.web_driver.current_url)  #debugging !!!

    def create_acc(self):

        web_driver.get(base_url)
        web_driver.implicitly_wait(10)

        sign_in_btn = self.web_driver.find_element(By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/a')
        print(f'Element located using XPATH assigned to the Sign In button{sign_in_btn}')
        sign_in_btn2 = web_driver.find_element(By.CSS_SELECTOR, "div[class='panel header'] li[data-label='or'] a")
        print(f'Element located using CSS SELECTOR assigned to the Sign In button{sign_in_btn2}')

        create_account_btn = self.web_driver.find_element(By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[3]/a')
        print(f'Element located using XPATH assigned to the ‘Create Account’ button.{create_account_btn}')
        create_account_btn.click()
        time.sleep(3)

        first_name_field = self.web_driver.find_element(By.XPATH, '//*[@id="firstname"]')
        first_name_field.send_keys(username)
        time.sleep(3)


        last_name_field = self.web_driver.find_element(By.XPATH, '//*[@id="lastname"]')
        last_name_field.send_keys(surname)
        time.sleep(3)

        email_field = self.web_driver.find_element(By.XPATH, '//*[@id="email_address"]')
        email_field.send_keys(user_email)
        time.sleep(3)

        user_password = self.web_driver.find_element(By.XPATH, '//*[@id="password"]')
        user_password.send_keys(password)
        time.sleep(3)

        user_password_cfrm = self.web_driver.find_element(By.XPATH,'//*[@id="password-confirmation"]')
        user_password_cfrm.send_keys(password)
        time.sleep(3)

        crt_acc_btn = self.web_driver.find_element(By.XPATH, '//*[@id="form-validate"]/div/div[1]/button')
        crt_acc_btn.click()
        time.sleep(5)

    def log_out(self):

        account_welcome_btn = self.web_driver.find_element(By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button')
        account_welcome_btn.click()
        time.sleep(2.5)

        sign_out_popup = self.web_driver.find_element(By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[3]/a')
        sign_out_popup.click()
        time.sleep(2.5)


    def sign_in(self):

        # sigin in

        sign_in_btn = self.web_driver.find_element(By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/a')
        print(f'Element located using XPATH assigned to the Sign In button{sign_in_btn}')
        sign_in_btn.click()
        time.sleep(3)

        sign_in_email = self.web_driver.find_element(By.XPATH, '//*[@id="email"]')
        sign_in_email.send_keys(user_email)
        time.sleep(2)

        sign_in_password = self.web_driver.find_element(By.XPATH, '//*[@id="pass"]')
        sign_in_password.send_keys(password)
        time.sleep(2.5)

        sign_in_btn_cfrm = self.web_driver.find_element(By.XPATH, '//*[@id="send2"]')
        sign_in_btn_cfrm.click()
        time.sleep(2.5)



        # Wait a moment to see the effect
        time.sleep(10)
        input('wciśnij Enter aby zamknąć program')
        # Close the browser
        web_driver.quit()

create_account = CreateAccount()
create_account.create_acc()
create_account.log_out()
create_account.sign_in()

