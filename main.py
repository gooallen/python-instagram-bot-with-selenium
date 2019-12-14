from selenium import webdriver

class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")

InstaBot()
