from PROJECT.settings import By, Keys, WebDriverWait, expected_conditions as EC
from PROJECT.constant import DRIVER_PATH, WEBSITE_URL, USERNAME, PASSWORD, EMAIL, USER_URL
from PROJECT.tests.base_test import BaseTestCase

# 20 minutes.
"""
test_follow_other_accounts (PROJECT.tests.test_follow_others.TestFollowAccountsOrgs) ... ok

----------------------------------------------------------------------
Ran 1 test in 17.468s

OK
"""

class TestFollowAccountsOrgs(BaseTestCase):

    def test_follow_other_accounts(self):
        self.user_login()
        self.assertEqual(self.browser.title, 'Feed | LinkedIn')
        self.browser.implicitly_wait(3)

        jobs_xpath = '//a[@data-link-to="mynetwork"]'
        available_job_elem = self.browser.find_element(By.XPATH, jobs_xpath)
        available_job_elem.click()
        self.browser.implicitly_wait(2)    

        follow_button_xpath = '//button[@class="artdeco-button artdeco-button--2 artdeco-button--full artdeco-button--secondary ember-view full-width"]'  
        wait_for_element_loading = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, follow_button_xpath))
        ) 
        follow_btn_elems = self.browser.find_elements(By.XPATH, follow_button_xpath)

        for follow_btn_elem in follow_btn_elems:
            if follow_btn_elem.text == 'Follow':
                follow_btn_elem.click()
                self.browser.implicitly_wait(2)
                break
        