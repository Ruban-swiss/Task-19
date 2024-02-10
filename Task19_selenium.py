from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class Task19:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(10)

    def quit(self):
        self.driver.quit()

    def login(self):
        username_input= self.driver.find_element(by=By.ID, value="user-name")
        password_input = self.driver.find_element(by=By.ID, value="password")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")

        self.driver.find_element(by=By.ID, value="login-button").click()

        sleep(10)

    def getTitle(self):
        return self.driver.title

    def getURL(self):
        return self.driver.current_url

    def sourceCode(self, filename="webpage_task_11.txt"):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.driver.page_source)
        return self.driver.page_source


url = "https://www.saucedemo.com/"
obj = Task19(url)
obj.boot()
obj.login()
print(obj.getURL())
print(obj.getTitle())
print(obj.sourceCode())
obj.quit()


