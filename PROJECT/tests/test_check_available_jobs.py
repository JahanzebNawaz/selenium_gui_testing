from PROJECT.settings import By, Keys, WebDriverWait, expected_conditions as EC
from PROJECT.constant import DRIVER_PATH, WEBSITE_URL, USERNAME, PASSWORD, EMAIL, USER_URL
from PROJECT.tests.base_test import BaseTestCase


# 1 and half hour.
"""
test_available_jobs (PROJECT.tests.test_check_available_jobs.TestAvailableJobs) ... ok

----------------------------------------------------------------------
Ran 1 test in 14.197s

OK
"""


class TestAvailableJobs(BaseTestCase):

    def test_available_jobs(self):
        self.user_login()
        # self.browser.get(WEBSITE_URL)
        self.assertEqual(self.browser.title, 'Feed | LinkedIn')
        self.browser.implicitly_wait(3)

        jobs_xpath = '//a[@data-link-to="jobs"]'
        available_job_elem = self.browser.find_element(By.XPATH, jobs_xpath)
        available_job_elem.click()
        self.browser.implicitly_wait(2)        