# Login Example based on https://github.com/Element-34/Py.Saunter-Examples
from scripts.Suite101BaseTestCase import Suite101BaseTestCase
from pages.HomePage import HomePage
import pytest


class CheckLoginExample(Suite101BaseTestCase):
    bad_password = "Error message Sorry, unrecognized username or password. Have you forgotten your password?"

    @pytest.marks('deep', 'sauce', 'login')
    def test_incorrect_login(self):
        h = HomePage()
        h.open_default_url()
        l = h.go_to_login_page()
        l.username = "foo"
        l.password = "bar"
        l.do_login()
        self.matchers.assert_equal(l.error_message, self.bad_password)

    @pytest.marks('deep', 'sauce', 'login')
    def test_incorrect_login_with_soft_assert(self):
        h = HomePage()
        h.open_default_url()
        l = h.go_to_login_page()
        l.username = "foo"
        l.password = "bar"
        l.do_login()
        self.matchers.verify_equal(l.error_message, self.bad_password)

    @pytest.marks('deep', 'sauce', 'login')
    def test_incorrect_login_with_random_username_and_password(self):
        h = HomePage()
        h.open_default_url()
        l = h.go_to_login_page()

        from saunter.generators.string_data import random_string
        l.username = random_string(5)
        l.password = random_string()

        l.do_login()
        self.matchers.assert_equal(l.error_message, self.bad_password)
