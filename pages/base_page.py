from selenium.webdriver.common.by import By
import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.saucedemo.com/'
        self.name = 'user-name'

    def visit(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        time.sleep(2)
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def user_element(self, name):
        time.sleep(2)
        return self.driver.find_element(By.CLASS_NAME, name)

    def pass_element(self, id):
        time.sleep(2)
        return self.driver.find_element(By.ID, id)
