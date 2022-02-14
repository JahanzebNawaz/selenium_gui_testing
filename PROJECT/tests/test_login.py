from .base_test import BaseTestCase
from PROJECT.settings import By, Keys, WebDriverWait, expected_conditions
from PROJECT.constant import USERNAME, PASSWORD, EMAIL


# it took me 2 hours setting up the test suit and test login test case
"""
testLoginToAccount (PROJECT.tests.test_login.TestLinkedInLogin)
User login UnitTest, test login to account ... ok

----------------------------------------------------------------------
Ran 1 test in 12.457s

OK
"""


class TestLinkedInLogin(BaseTestCase):

    def testLoginToAccount(self):
        """User login UnitTest, test login to account"""
        self.browser.get(self.website_url)
        self.assertIn('LinkedIn: Log In or Sign Up', self.browser.title)
        self.assertIn('https://www.linkedin.com/', self.browser.current_url)

        email_elem = self.browser.find_element(By.NAME, "session_key")
        email_elem.send_keys(EMAIL)

        passowrd_elem = self.browser.find_element(By.NAME, "session_password")
        passowrd_elem.send_keys(PASSWORD)
        login_button_elem = self.browser.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
        self.browser.implicitly_wait(2)
        login_button_elem.click()
        self.assertIn('Feed | LinkedIn', self.browser.title)
        self.assertIn('https://www.linkedin.com/feed/?trk=homepage-basic_signin-form_submit', self.browser.current_url)

