"""
Experience Page Object
"""
from saunter.po.remotecontrol.text import Text
from saunter.SeleniumWrapper import SeleniumWrapper as wrapper

from pages.Suite101BasePage import Suite101BasePage

# locators are a mapping from page sections/items to selectors (xpath/css/etc)
# define here ONLY, so we only ever have to change them in one place.
locators = {
    "experience_title": "",
    "experience_in_response_to": "",
    "experience_me_too_button": "",
    "experience_image": "",
    "experience_add_image_button": "",
    "experience_author_image": "",
    "experience_author_description": "",
    "experience_author_name": "",
    "experience_follow_button": "",
    "experience_share_twitter_button": "",
    "experience_share_facebook_button": "",
    "experience_add_chapter_button": "",
    "experience_page_add_chapter_title": "",
    "experience_page_add_chapter_body": "",
    "experience_page_add_chapter_submit": "",
}


class AddChapterTitleElement(Text):
    def __init__(self):
        self.locator = locators["experience_page_add_chapter_title"]


class AddChapterBodyElement(Text):
    def __init__(self):
        self.locator = locators["experience_page_add_chapter_body"]


class ExperiencePage(Suite101BasePage):
    """
    Page Object for the Experience Detail Page
    """
    add_chapter_title = AddChapterTitleElement()
    add_chapter_body = AddChapterBodyElement()

    def __init__(self):
        self.se = wrapper().connection
