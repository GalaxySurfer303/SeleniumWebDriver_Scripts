from selenium import webdriver
import time

# Tworzenie instancji Safari WebDriver
driver = webdriver.Safari()
driver.get("https://www.example.com")
time.sleep(2)  # Czekaj chwilę, aby zobaczyć stronę

driver.quit()