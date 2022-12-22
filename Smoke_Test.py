import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import Fakers as locators
s=Service(executable_path='./chromedriver')
driver=webdriver.Chrome(service=s)


# Fixture method - to open web browser
def setUp():
    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the Moodle app website
    driver.get(locators.moodle_url)

    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.moodle_url and driver.title == 'CCTB PBLMT SQTA Bootcamp':
        print(f'We\'re at Moodle homepage -- {driver.current_url}')
        print(f'We\'re seeing title message -- {driver.title}')
    else:
        print('We\'re not at the Moodle homepage. Check your code!')
        driver.close()
        driver.quit()