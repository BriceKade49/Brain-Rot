from selenium import webdriver
import time
def run_Hulu(episode_url):
    username = "bdk4949@outlook.com"
    password = "TechStars"

    url = "https://auth.hulu.com/web/login"

    driver = webdriver.Chrome("../chromedriver.exe")

    driver.get(url)
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_class_name("login-button").click()

    time.sleep(3)
    driver.get(episode_url)
    time.sleep(5) # if not working time.sleep(13)

    driver.find_element_by_class_name("PlaybackControlsOverPlayer").click()

    print("worked")