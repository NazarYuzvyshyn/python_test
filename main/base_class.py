from selenium import webdriver


class BaseClass:

    def __init__(self, driver: webdriver):
        self.driver = driver