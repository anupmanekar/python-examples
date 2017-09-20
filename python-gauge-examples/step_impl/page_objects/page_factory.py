from getgauge.python import before_suite, after_suite
from selenium import webdriver

from step_impl.page_objects.google_page import GooglePage

class PageFactory:
    driver = None
    google_page = None


@before_suite
def init():
    PageFactory.driver = webdriver.Chrome()
    PageFactory.google_page = GooglePage(PageFactory.driver)


@after_suite
def close():
    PageFactory.driver.close()