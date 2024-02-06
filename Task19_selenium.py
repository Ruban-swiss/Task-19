from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class LoginAutomation:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.sleep(5)

    def sleep(self, seconds):
        sleep(seconds)

    def inputBox(self, value, key):
        self.driver.find_element(by=By.NAME, value=value).send_keys(key)

    def submitBtn(self):
        self.driver.find_element(by=By.TAG_NAME, value="button").click()

    def quit(self):
        self.driver.quit()


    def fetch_title(self):
            self.driver.get(self.url)
            return self.driver.title


    def fetchURL(self):
        try:
            print(self.findElement().get_attribute("href"))
        except:
            print("unable to fetch the url")

    def fetch_entire_contents(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.driver.page_source)

    def fetch_webpage_info(self):
        title = self.fetch_title()
        self.fetch_entire_contents("webpage_task_11.txt")
        self.driver.quit()

    def login(self):
        self.boot()
        self.inputBox("username", self.username)
        self.inputBox("password",self.password)
        self.submitBtn()

url = "https://www.saucedemo.com/"

obj = LoginAutomation(url, username="standard_user", password="secret_sauce")
obj.login()
obj.boot()
obj.fetch_title()
obj.fetchURL()
obj.fetch_entire_contents()
obj.fetch_webpage_info()
obj.quit()

print("Title:", title)
print("Webpage content saved to 'webpage_task_11.txt'")