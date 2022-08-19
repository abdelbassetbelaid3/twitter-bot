from cgitb import text
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class bot:
    def __init__(self, email, password, user_name="", driver_path=r'D:/SeleniumDrivers/chromedriver.exe', profile=r"C:\Users\abdel\AppData\Local\Google\Chrome\User Data",
                 user_data="C:\\Users\\abdel\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1", teardown=False) -> None:
        self.email = email  # email
        self.user_name = user_name  # user name
        self.password = password  # password
        self.driver_path = driver_path
        self.chrome_profile = profile
        self.user_data = user_data
        self.teardown = teardown
        self.init()
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument(
            f"user-data-dir={self.user_data}")
        self.driver = webdriver.Chrome(
            executable_path=self.driver_path, chrome_options=options)
        super(bot, self).__init__()

    def init(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def login_page(self):
        bot = self.driver
        bot.get("https://twitter.com/i/flow/login")
        bot.implicitly_wait(30)
        user = bot.find_element(By.NAME, "text")
        user.send_keys(self.email)
        user.send_keys(Keys.RETURN)
        secruity = bot.find_element(By.NAME, "text")
        print(secruity)
        if secruity.text == "":
            secruity.send_keys(self.user_name)
            secruity.send_keys(Keys.RETURN)
        password = bot.find_element(By.NAME, "password")
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        sleep(5)

    def hashTag(self, tag: str):
        bot = self.driver
        bot.get("https://twitter.com/search?q=%23" + tag +
                "&src=typeahead_click&f=live")
