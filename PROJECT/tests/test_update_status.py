from PROJECT.settings import By, WebDriverWait, expected_conditions as EC
from PROJECT.constant import DRIVER_PATH, WEBSITE_URL, USERNAME, PASSWORD, EMAIL, USER_URL
from PROJECT.tests.base_test import BaseTestCase


# 1 and half hour.

"""
test_login_to_account (PROJECT.tests.test_update_status.TestUpdateProfileStatus) ... ok

----------------------------------------------------------------------
Ran 1 test in 21.291s

OK
"""


class TestUpdateProfileStatus(BaseTestCase):

    def test_login_to_account(self):
        self.user_login()
        self.browser.get(WEBSITE_URL + USER_URL)
        self.assertEqual(self.browser.title, 'Jake (James) Willim | LinkedIn')
        self.browser.implicitly_wait(3)

        open_button_xpath = '//div[@class="artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-left ember-view pv-top-card-add-goals mr2"]'
        status_elem = self.browser.find_element(By.XPATH, open_button_xpath)
        status_elem.click()
        self.browser.implicitly_wait(2)

        options_xpath = '//div[@class="artdeco-dropdown__item artdeco-dropdown__item--is-dropdown ember-view pv-top-card-add-goals__list-item"]'
        option_elem = self.browser.find_element(By.XPATH, options_xpath)
        option_elem.click()

        self.browser.implicitly_wait(2)


        wait_for_elem = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@data-test-fb-pill="Hybrid"]'))
        )
        
        hybrid_button = self.browser.find_element(By.XPATH, '//button[@data-test-fb-pill="Hybrid"]')
        hybrid_button.click()
        self.browser.implicitly_wait(1)

        remote_button = self.browser.find_element(By.XPATH, '//button[@data-test-fb-pill="Remote"]')
        remote_button.click()
        self.browser.implicitly_wait(1)


        contract_button = self.browser.find_element(By.XPATH, '//button[@data-test-fb-pill="Contract"]')
        contract_button.click()

        visibility_elem = self.browser.find_element(By.XPATH, '//button[@class="vb-visibility-dropdown__otw-trigger text-align-left artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-top ember-view"]')
        visibility_elem.click()

        self.browser.implicitly_wait(1)
        public_option = self.browser.find_element(By.XPATH, '//label[@data-test-visibility-dropdown-item="LOGGED_IN_MEMBERS"]')
        public_option.click()

        self.browser.implicitly_wait(1)

        apply_button = self.browser.find_element(By.XPATH, '//button[@class="fr artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]')
        apply_button.click()


        thanks_button = self.browser.find_element(By.XPATH, '//button[@class="mr1 artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view"]')
        thanks_button.click()

        profile_name = self.browser.find_element(By.XPATH, "//h1[@class='text-heading-xlarge inline t-24 v-align-middle break-words']")
        self.assertIn('Jake (James) Willim', profile_name.text)

