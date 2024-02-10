from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class WebPageFetcher:
    
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def login(self):
        try:
            self.driver.get(self.url)
            username_input = self.driver.find_element(By.ID, "user-name")
            password_input = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.ID, "login-button")

            username_input.send_keys(self.username)
            password_input.send_keys(self.password)
            login_button.click()
        except WebDriverException as e:
            print("Exception occurred while logging in:", e)

    def save_webpage_content(self, filename):
        try:
            with open(filename, "w") as f:
                f.write(self.driver.page_source)
        except WebDriverException as e:
            print("Exception occurred while saving webpage content:", e)

    def quit(self):
        self.driver.quit()

# URL and credentials
url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"

# Create instance of WebPageFetcher and perform tasks
webpage_fetcher = WebPageFetcher(url, username, password)
webpage_fetcher.login()

# Task 3: Extract entire contents of the webpage and save it in a text file
webpage_fetcher.save_webpage_content("webpage_task_11.txt")

# Quit the driver
webpage_fetcher.quit()
