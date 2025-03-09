import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class InstaFollower:
    def __init__(self, chrome_options, driver_path):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(driver_path)

    def login(self, username, passw):
        #Click to deny cookies
        button = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Decline optional cookies')]")
        button.click()

        #Enter login and password
        login = self.driver.find_element(By.NAME, value="username")
        login.send_keys(username)
        time.sleep(2)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(passw)
        time.sleep(1)
        password.send_keys(Keys.ENTER)

        #In case that would appear any pop-up after login
        input("Click enter when you are logged in")


    def find_followers(self, account):
        #go to the selected account
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{account}/")

        #open the followers
        time.sleep(3)
        followers = self.driver.find_element(By.XPATH, value='//span[text()=" followers"]')
        followers.click()

        time.sleep(3)
        list_of_followers = self.driver.find_element(By.XPATH, value='/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", list_of_followers)
            time.sleep(2)

    def follow(self):
        pass