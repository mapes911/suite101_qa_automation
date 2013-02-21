"""
Experiences Test Suite

Creation
Editing
Adding Chapters
Related Experiences
Commenting
Following

"""

from scripts.Suite101BaseTestCase import Suite101BaseTestCase
from pages.HomePage import HomePage

# import pytest


class ExperienceTestSuite(Suite101BaseTestCase):
    """
    Experience Test Suite
    """

    def test_create_new_experience(self):
        """
        Create a new experience "from scratch", i.e. not from a "me too!" button
        """
        h = HomePage()
        h.open_default_url()
