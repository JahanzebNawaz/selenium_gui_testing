from PROJECT.settings import By, Keys, WebDriverWait, expected_conditions as EC
from PROJECT.constant import DRIVER_PATH, WEBSITE_URL, USERNAME, PASSWORD, EMAIL, USER_URL
from PROJECT.tests.base_test import BaseTestCase
import datetime

# 1.5 and half hour.

"""
test_add_feed_post (PROJECT.tests.test_add_feed_post.TestAddFeedPost) ... ok

----------------------------------------------------------------------
Ran 1 test in 14.707s

OK
"""


class TestAddFeedPost(BaseTestCase):

    def test_add_feed_post(self):
        self.user_login()
        # self.browser.get(WEBSITE_URL)
        self.assertEqual(self.browser.title, 'Feed | LinkedIn')
        self.browser.implicitly_wait(3)

        post_input_xpath = '//button[@class="artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view share-box-feed-entry__trigger"]'
        post_btn_elem = self.browser.find_element(By.XPATH, post_input_xpath)
        post_btn_elem.click()

        self.browser.implicitly_wait(2)

        date_time = datetime.datetime.now()

        text = 'Good morning folks! this is automated test post!'
        # document.querySelector('[role="textbox"]');
        # js_code_with_selector = f'document.querySelector(".ql-editor").innerText = "HAVE A GOOD DAY! {str(date_time)}";'
        js_code_with_selector = f'document.querySelector(\'[role="textbox"]\').innerText = "HAVE A GOOD DAY! {str(date_time)}";'

        input_elem = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]'))
        )

        self.browser.execute_script(js_code_with_selector)
        self.browser.implicitly_wait(10)

        apply_btn_xpath = '//button[@class="share-actions__primary-action artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]'
        wait_for_elem = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, apply_btn_xpath))
        )
        apply_btn_elem = self.browser.find_element(By.XPATH, apply_btn_xpath)
        apply_btn_elem.click()
        