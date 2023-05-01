from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class SwagLabs(BasePage):


    def exist_icon(self):
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True


    def welcomeUser(self):
        try:
            self.user_element(name='user-name')
        except NoSuchElementException:
            return False
        return True

    def welPass(self):
        try:
            self.pass_element(id='password')
        except NoSuchElementException:
            return False
        return True
