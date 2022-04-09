from selenium import webdriver
import time

username = "bdk4949@outlook.com"
password = "TechStars"

url = "https://www.netflix.com/login"
# title = ""
# season = input()
# episode = input()

driver = webdriver.Chrome("chromedriver.exe")

driver.get(url)
driver.find_element_by_name("userLoginId").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_css_selector(".login-button.btn").click()
time.sleep(1)
driver.find_element_by_class_name('profile-icon').click()
driver.get("https://www.netflix.com/watch/81218414?source=35")
time.sleep(1)
driver.find_element_by_css_selector("button, html input[type=button], input[type=reset], input[type=submit]").click()
driver.find_element_by_link_text("Play").click()

print("worked")
