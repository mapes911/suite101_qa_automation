"""
Login Page Object
"""
from saunter.po.remotecontrol.text import Text
from saunter.po import string_timeout
from saunter.SeleniumWrapper import SeleniumWrapper as wrapper

from pages.Suite101BasePage import Suite101BasePage

locators = {
    "username": "edit-name",
    "password": "edit-pass",
    "submit_button": "edit-submit",
    "error_message": "css=div.messages.error"
}


class UsernameTextElement(Text):
    def __init__(self):
        self.locator = locators["username"]


class PasswordTextElement(Text):
    def __init__(self):
        self.locator = locators["password"]


class ErrorMessageTextElement(Text):
    def __init__(self):
        self.locator = locators["error_message"]


class LoginPage(Suite101BasePage):
    #: username text field
    username = UsernameTextElement()
    #: password text field
    password = PasswordTextElement()
    #: incorrect login message
    error_message = ErrorMessageTextElement()

    def __init__(self):
        self.se = wrapper().connection

    def do_login(self):
        """
        Does the form submission
        """
        self.se.click(locators['submit_button'])
        self.se.wait_for_page_to_load(string_timeout)
