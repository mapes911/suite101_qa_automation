"""
Home Page Object
"""
from saunter.po import string_timeout
from saunter.SeleniumWrapper import SeleniumWrapper as wrapper

from pages.LoginPage import LoginPage
from pages.Suite101BasePage import Suite101BasePage

locators = {
    "login": 'xpath=(//a[text()="Login"])[1]',
    "signup": 'xpath=(//a[text()="Signup"])[1]'
}


class HomePage(Suite101BasePage):
    """
    PO for the Home/Landing page
    """
    def __init__(self):
        self.se = wrapper().connection

    def open_default_url(self):
        """
        Goes to the default url for this PO
        """
        self.se.open("/")

    def go_to_login_page(self):
        """
        Goes to the login page

        :returns: :class:`pages.LoginPage.LoginPage`
        """
        self.se.click(locators['login'])
        self.se.wait_for_page_to_load(string_timeout)
        return LoginPage()
