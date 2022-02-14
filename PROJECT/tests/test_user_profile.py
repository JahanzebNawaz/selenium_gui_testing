from PROJECT.settings import By, WebDriverWait, expected_conditions, webdriver
from PROJECT.constant import DRIVER_PATH, WEBSITE_URL, USERNAME, PASSWORD, EMAIL, USER_URL
from PROJECT.tests.base_test import BaseTestCase

# 4 Hours due to couple of debugging and repetation of testing.
"""
test_login_to_account (PROJECT.tests.test_user_profile.TestPersonProfile) ... ok

----------------------------------------------------------------------
Ran 1 test in 19.924s

OK
"""

class TestPersonProfile(BaseTestCase):

    def test_login_to_account(self):
        self.user_login()
        # it open the User profile options.
        profile_elem = self.browser.find_element(By.ID, "ember25")
        self.browser.implicitly_wait(2)
        profile_elem.click()

        self.browser.implicitly_wait(2)
        profile_link_xpath = '/html/body/div[7]/header/div/nav/ul/li[6]/div/div/div/header/a[2]'
        
        elem_email = WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, profile_link_xpath))
        )

        elem_email.click()
        self.browser.implicitly_wait(2)
        self.assertEqual(self.browser.title, 'Feed | LinkedIn')
        # redirect to the user update form
        self.browser.get(WEBSITE_URL + USER_URL + 'edit/forms/intro/new/?profileFormEntryPoint=PROFILE_SECTION')
        self.browser.implicitly_wait(2)

        input_field_id = "single-line-text-form-component-profileEditFormElement-TOP-CARD-profile-ACoAADoFea0B0hnu-GPXoBu4Oackx4l1oMZQg1s-maidenName"
        aditional_name_elem = self.browser.find_element(By.ID, input_field_id)
        aditional_name_elem.click()
        aditional_name_elem.clear()
        aditional_name_elem.send_keys("James")

        save_button_class = "//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view']"
        save_button_elem = self.browser.find_element(By.XPATH, save_button_class)
        save_button_elem.click()
        self.browser.implicitly_wait(2)
        self.browser.refresh()
        profile_name = self.browser.find_element(By.XPATH, "//h1[@class='text-heading-xlarge inline t-24 v-align-middle break-words']")
        self.assertIn('Jake (James) Willim', profile_name.text)

