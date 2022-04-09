from selenium import webdriver
import time

username = "bdk4949@outlook.com"
password = "TechStars1"

url = "https://www.disneyplus.com/login"

episode_url = "https://www.disneyplus.com/video/0e8e7f27-0ab2-495f-8254-d99d3c53ce4f"

driver = webdriver.Chrome("chromedriver.exe")

driver.get(url)
time.sleep(3)
driver.find_element_by_name("email").send_keys(username)
driver.find_element_by_name("dssLoginSubmit").click()
time.sleep(3)

driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("dssLoginSubmit").click()
time.sleep(3)

driver.get(episode_url)
time.sleep(10)
#driver.find_element_by_css_selector("button, html input[type=button], input[type=reset], input[type=submit]").click()
driver.find_element_by_link_text("play").click()


print("worked")
