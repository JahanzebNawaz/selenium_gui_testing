from PROJECT.settings import By, Keys, WebDriverWait, expected_conditions as EC
from PROJECT.constant import DRIVER_PATH, WEBSITE_URL, USERNAME, PASSWORD, EMAIL, USER_URL
from PROJECT.tests.base_test import BaseTestCase

# 20 minutes.

"""
test_like_others_feed (PROJECT.tests.test_like_others_feed.TestLikeOthersFeed) ... ok

----------------------------------------------------------------------
Ran 1 test in 13.562s

OK
"""

class TestLikeOthersFeed(BaseTestCase):

    def test_like_others_feed(self):
        self.user_login()
        self.assertEqual(self.browser.title, 'Feed | LinkedIn')
        self.browser.implicitly_wait(3)

        feeds_xpath = '//div[@class="scaffold-finite-scroll__content"]'
        feeds_elem = self.browser.find_element(By.XPATH, feeds_xpath)
        like_btn_xpath = '//span[@class="reactions-react-button feed-shared-social-action-bar__action-button"]'

        wait_for_element_loading = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, like_btn_xpath))
        ) 
        likes_feed_elems = self.browser.find_elements(By.XPATH, like_btn_xpath)

        for like_button in likes_feed_elems:
            like_button.click()
            self.browser.implicitly_wait(3)
            break
 