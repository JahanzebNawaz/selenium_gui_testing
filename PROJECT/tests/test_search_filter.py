from PROJECT.settings import By, Keys, WebDriverWait, expected_conditions as EC
from PROJECT.constant import DRIVER_PATH, WEBSITE_URL, USERNAME, PASSWORD, EMAIL, USER_URL
from PROJECT.tests.base_test import BaseTestCase


# 1 and half hour.
"""
test_search_by_text (PROJECT.tests.test_search_filter.TestSearchFilter) ... ok

----------------------------------------------------------------------
Ran 1 test in 20.581s

OK
"""


class TestSearchFilter(BaseTestCase):

    def test_search_by_text(self):
        self.user_login()
        self.browser.get(WEBSITE_URL)
        self.assertEqual(self.browser.title, 'Feed | LinkedIn')
        self.browser.implicitly_wait(3)

        search_input_xpath = '//input[@placeholder="Search"]'
        search_elem = self.browser.find_element(By.XPATH, search_input_xpath)
        search_elem.click()
        search_elem.send_keys('Python Developer')
        search_elem.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(2)


        search_filter_xpath = '//button[@aria-label="People"]'
        input_elem = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, search_filter_xpath))
        )
        search_filter_elem = self.browser.find_element(By.XPATH, search_filter_xpath)
        search_filter_elem.click()
        self.browser.implicitly_wait(2)
        