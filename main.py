import os
from selenium import webdriver
from Instagram import InstaFollower

INSTAGRAM_USER = os.environ["INSTAGRAM_USER"]
INSTAGRAM_PASS = os.environ["INSTAGRAM_PASS"]
SIMILAR_ACCOUNT = "j.codesfullstack"
CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option("detach", True)
DRIVER_PATH = "https://www.instagram.com/?flo=true"

bot = InstaFollower(CHROME_OPTIONS, DRIVER_PATH)
bot.login(INSTAGRAM_USER, INSTAGRAM_PASS)
bot.find_followers(SIMILAR_ACCOUNT)
bot.follow()