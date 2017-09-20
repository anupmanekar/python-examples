from selenium.webdriver.common.by import By

from step_impl.page_objects.base_page import BasePage


class GooglePageLocators:
    SEARCH_FIELD = (By.ID, 'lst-ib')
    SEARCH_BTN = (By.CSS_SELECTOR, 'input[value="Google Search"]')
    FIRST_RESULT = (By.CSS_SELECTOR,'h3.r a')

class GooglePage(BasePage):
    URL = '{}'.format('https://www.google.com')

    def search(self, term):
        self.set(GooglePageLocators.SEARCH_FIELD, term)
        self.click(GooglePageLocators.SEARCH_BTN)

    def visit(self):
        print(self.URL)
        self.driver.get(self.URL)
        
    def get_first_result(self):
        return self.get(GooglePageLocators.FIRST_RESULT)