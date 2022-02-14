from PROJECT.settings import By, WebDriverWait, expected_conditions as EC
from PROJECT.constant import DRIVER_PATH, WEBSITE_URL, USERNAME, PASSWORD, EMAIL, USER_URL
from PROJECT.tests.base_test import BaseTestCase


# 3 and half hour.
"""
test_new_experience_to_account (PROJECT.tests.test_add_new_experience.TestAddExperienceToProfile) ... ok

----------------------------------------------------------------------
Ran 1 test in 19.231s

OK
"""


class TestAddExperienceToProfile(BaseTestCase):

    def test_new_experience_to_account(self):
        self.user_login()
        self.browser.get(WEBSITE_URL + USER_URL)
        self.assertEqual(self.browser.title, 'Jake (James) Willim | LinkedIn')
        self.browser.implicitly_wait(3)

        experience_bth_xpath = '//li-icon[@aria-label="Add new experience"]'
        experience_btn_elem = self.browser.find_element(By.XPATH, experience_bth_xpath)
        experience_btn_elem.click()
        self.browser.implicitly_wait(10)



        add_title_xpath = '//input[@id="single-typeahead-entity-form-component-profileEditFormElement-POSITION-profilePosition-ACoAADoFea0B0hnu-GPXoBu4Oackx4l1oMZQg1s-1-title"]'
        title_elem = self.browser.find_element(By.XPATH, add_title_xpath)
        title_elem.click()
        title_elem.clear()
        title_elem.send_keys('Software Engineer')

        self.browser.implicitly_wait(10)

        add_company_xpath = '//input[@id="single-typeahead-entity-form-component-profileEditFormElement-POSITION-profilePosition-ACoAADoFea0B0hnu-GPXoBu4Oackx4l1oMZQg1s-1-requiredCompany"]'
        company_elem = self.browser.find_element(By.XPATH, add_company_xpath)
        company_elem.click()
        company_elem.clear()
        company_elem.send_keys('FANG')

        self.browser.implicitly_wait(2)
        add_month_xpath = '//select[@name="month"]'
        month_elem = self.browser.find_element(By.XPATH, add_month_xpath)
        month_elem.send_keys('January')

        self.browser.implicitly_wait(2)
        add_year_xpath = '//select[@name="year"]'
        year_elem = self.browser.find_element(By.XPATH, add_year_xpath)
        year_elem.send_keys('2018')

        apply_button = self.browser.find_element(By.XPATH, '//button[@class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]')
        apply_button.click()
        