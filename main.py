# Importing the required modules for Selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# By using time module we are going to increase the on screen time
import time

# Setting your chromedriver path
CHROME_PATH = "/Users/Cassa/chromedriver"

# Setting the account whose followers you wish to follow
ACCOUNT = 'python.hub'

# Setting the website URL
URL = 'https://www.instagram.com/'

# Intialising the class
class Instagram:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH)

    # Method to login into the instagram account
    def login(self):
        self.driver.get(URL+'accounts/login/')
        time.sleep(6)

        # Username input automation
        username = self.driver.find_element_by_name('username')
        username.send_keys('your_username/email_id@example.com')
        time.sleep(2)

        # Password input automation
        password = self.driver.find_element_by_name('password')
        password.send_keys('your_password')
        time.sleep(2)

        # To proceed
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        # At this point it may ask you to safe your login info, However that is completely optional

    # Method to find the followers of desired account
    def find_followers(self):

        # Getting URL of desired account
        self.driver.get(URL+ACCOUNT)

        # Getting the followers
        follow = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        follow.click()
        time.sleep(3)

        # From here since popup will show only 15 followers on the screen, Below is a Javascript Code
        # To load more followers by scrolling the sidebar upwards
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        for i in range(10):  # Adjust the range according to number of followers you wish to follow
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', modal)
            time.sleep(3)

    # Method to follow the listed followers
    def follow(self):
        follow_buttons = self.driver.find_elements_by_css_selector('li button')
        for follow_button in follow_buttons:
            follow_button.click()
            time.sleep(2)

# Initialising our bot
insta_bot = Instagram()

# To login into your account
insta_bot.login()

# To find all required number of followers
insta_bot.find_followers()

# To follow them individually
insta_bot.follow()
