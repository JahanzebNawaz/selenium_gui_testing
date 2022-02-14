from PROJECT.settings import By, WebDriverWait, expected_conditions as EC
from PROJECT.constant import DRIVER_PATH, WEBSITE_URL, USERNAME, PASSWORD, EMAIL, USER_URL
from PROJECT.tests.base_test import BaseTestCase


# 1 and half hour.
"""
test_new_section_to_account (PROJECT.tests.test_add_new_section.TestAddSectionToProfile) ... ok

----------------------------------------------------------------------
Ran 1 test in 19.784s

OK
"""


class TestAddSectionToProfile(BaseTestCase):

    def test_new_section_to_account(self):
        self.user_login()
        self.browser.get(WEBSITE_URL + USER_URL)
        self.assertEqual(self.browser.title, 'Jake (James) Willim | LinkedIn')
        self.browser.implicitly_wait(3)

        # add_section_button_xpath = '//button[@class="artdeco-button artdeco-button--2 artdeco-button--secondary ember-view mr2"]'
        add_section_button_elem =  '//div[@class="pv-top-card-v2-ctas pt2 display-flex"]//button[@class="artdeco-button artdeco-button--2 artdeco-button--secondary ember-view mr2"]'
        section_elem = self.browser.find_element(By.XPATH, add_section_button_elem)
        section_elem.click()
        self.browser.implicitly_wait(2)


        add_info_button = self.browser.find_element(By.LINK_TEXT, 'Add about')
        add_info_button.click()
        self.browser.implicitly_wait(2)

        textarea_field_xpath = '//textarea[@class="fb-multiline-text  artdeco-text-input--input artdeco-text-input__textarea artdeco-text-input__textarea--align-top"]'
        write_info_elem = self.browser.find_element(By.XPATH, textarea_field_xpath)
        write_info_elem.click()
        write_info_elem.clear()
        write_info_elem.send_keys('I am a test user')
        self.browser.implicitly_wait(2)

        self.browser.implicitly_wait(1)

        apply_button = self.browser.find_element(By.XPATH, '//button[@class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]')
        apply_button.click()
        