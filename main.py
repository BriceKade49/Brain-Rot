from selenium import webdriver
import time

playlist = []

def run_Hulu(episode_url):
    username = "bdk4949@outlook.com"
    password = "TechStars"

    url = "https://auth.hulu.com/web/login"

    driver = webdriver.Chrome("chromedriver.exe")

    driver.get(url)
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_class_name("login-button").click()

    time.sleep(3)
    driver.get(episode_url)
    time.sleep(5) # if not working time.sleep(13)

    driver.find_element_by_class_name("PlaybackControlsOverPlayer").click()
    not_over = True
    while not_over:
        # print(driver.find_element_by_class_name("time-display-label body-copy").text)
        cur_time = int(driver.find_element_by_class_name("Timeline__slider").get_attribute("aria-valuenow"))
        end_time = int(driver.find_element_by_class_name("Timeline__slider").get_attribute("aria-valuemax"))
        if cur_time >= end_time - end_time * 0.1:
            break

    return


def run_DisneyPlus(episode_url):
    username = "bdk4949@outlook.com"
    password = "TechStars1"

    url = "https://www.disneyplus.com/login"

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
    time.sleep(15)
    #disney automatically plays
    #driver.find_element_by_link_text("play").click()
    while True:
        end_time = float(driver.find_element_by_class_name("progress-bar").find_element_by_class_name("slider-container").get_attribute("aria-valuemax"))
        cur_time = float(driver.find_element_by_class_name("progress-bar").find_element_by_class_name("slider-container").get_attribute("aria-valuenow"))
        if cur_time >= end_time - end_time * 0.1:
            break

    driver.close()
    return
def run_Netflix(show_url, season_num, episode_num):
    username = "bdk4949@outlook.com"
    password = "TechStars"

    url = "https://www.netflix.com/login"

    driver = webdriver.Chrome("chromedriver.exe")

    driver.get(url)
    driver.find_element_by_name("userLoginId").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector(".login-button.btn").click()
    time.sleep(3)
    driver.find_element_by_class_name('profile-icon').click()
    driver.get("https://www.netflix.com/watch/80133434?trackId=14277283&tctx=-97%2C-97%2C%2C%2C%2C%2C%2C")
    time.sleep(10)
    driver.find_element_by_css_selector("button, html input[type=button], input[type=reset], input[type=submit]").click()
    driver.find_element_by_link_text("Play").click()



    while True:
        cur_time = driver.find_element_by_class_name("ltr-ycx6uv-progressRailCss").find_element_by_class_name(
            "ltr-l4hk9c-knobCss").get_attribute("aria-valuemax")
        end_time = driver.find_element_by_class_name("ltr-ycx6uv-progressRailCss").find_element_by_class_name(
            "ltr-l4hk9c-knobCss").get_attribute("aria-valuenow")
        if cur_time >= end_time - end_time * 0.1:
            break


def runPlaylist(playlist):
    for episode in playlist:
        playEpisode(episode)
    print("success")

def playEpisode(episode):
    if episode[0] == "hulu":
        run_Hulu(episode[1])
    elif episode[0] == "disneyplus":
        run_DisneyPlus(episode[1])
    elif episode[0] == "netflix":
        run_Netflix(episode[1], episode[2], episode[3])
    return

while True:
    platform = input("type platform name: ")
    show_url = input("type show name: ")
    season_num = int(input("type season number: "))
    episode_num = int(input("type episode number: "))
    this_is_last = int(input("Next episode?"))

    playlist.append([platform, show_url, season_num, episode_num])

    if this_is_last == 1:
        break


runPlaylist(playlist)



