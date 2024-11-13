import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service as Chrome_Service

#from PlayGround_demos.notes import driver

# motherfuckers = 'motherfuckers'
# fucking = 'fucking'
# print('hello %s , can you feel the %s bass' % (motherfuckers, fucking))


########################################################################
# test in the class form


class FirstSafariTest():
    def test(self):
        web_driver = webdriver.Safari()
        web_driver.get('https://www.letskodeit.com/practice')
        web_driver.implicitly_wait(10)

        # Get the height of the visible part of the browser window
        view_height = web_driver.execute_script("return window.innerHeight;")

        # Calculate the target scroll distance to be 3/4 of the visible window height
        # This determines how much of the page will be scrolled down in total
        scroll_target = int(view_height * 0.75)

        # Define the scroll step size by dividing the target scroll distance into 20 smaller steps
        # This allows us to scroll down gradually in smaller increments, creating a smooth scrolling effect
        scroll_step = int(scroll_target / 20)

        # Loop to perform smooth scrolling down by 3/4 of the visible page height
        for _ in range(20):  # perform 20 steps to reach the target scroll distance
            # Scroll down by the defined step size in each iteration
            web_driver.execute_script(f"window.scrollBy(0, {scroll_step});")
            # Wait briefly between each scroll step to make the scrolling appear smooth and gradual
            time.sleep(0.2)

        # Wait a moment to see the effect
        time.sleep(10)
        input('wciśnij Enter aby zamknąć program')
        # Close the browser
        web_driver.quit()

first_test = FirstSafariTest()
first_test.test()

