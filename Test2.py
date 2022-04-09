from selenium import webdriver
import time

username = "cabinsmack@icloud.com"
password = "11262001bd"

url = "https://www.netflix.com/login"
title = ""
season = 4
episode = 7

driver = webdriver.Chrome("chromedriver.exe")

driver.get(url)
driver.find_element_by_name("userLoginId").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_css_selector(".login-button.btn").click()
time.sleep(3)
driver.find_element_by_class_name('profile-icon').click()

# -- look for a season, find an episode, play the episode -- #
driver.get("https://www.netflix.com/watch/81341727?source=35")

time.sleep(1)
driver.find_element_by_css_selector("button, html input[type=button], input[type=reset], input[type=submit]")   # .click()
time.sleep(3)
driver.find_element_by_xpath("//button[@aria-label='Play']").click()

print("worked")