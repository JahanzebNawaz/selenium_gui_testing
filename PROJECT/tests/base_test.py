import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PROJECT.constant import WEBSITE_URL, DRIVER_PATH, USERNAME, PASSWORD, EMAIL, LOGOUT_URL
from PROJECT.settings import By
import pickle
import time


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.service = Service(DRIVER_PATH)
        self.website_url = WEBSITE_URL
        self.options = webdriver.ChromeOptions() 
        self.options.add_argument("user-data-dir=/home/jk/.config/google-chrome/Profile 4/Web Data")
        self.browser = webdriver.Chrome(service=self.service)
        self.browser.maximize_window()
        self.addCleanup(self.browser.quit)

    def tearDown(self):
        time.sleep(3)
        self.browser.get(LOGOUT_URL)
        self.browser.close()


    def user_login(self):
        self.browser.get(self.website_url)
        self.assertIn('LinkedIn: Log In or Sign Up', self.browser.title)
        self.assertIn('https://www.linkedin.com/', self.browser.current_url)

        # self.upload_cookies()
        # self.dump_cookies()

        email_elem = self.browser.find_element(By.NAME, "session_key")
        email_elem.send_keys(EMAIL)

        passowrd_elem = self.browser.find_element(By.NAME, "session_password")
        passowrd_elem.send_keys(PASSWORD)
        login_button_elem = self.browser.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
        self.browser.implicitly_wait(2)
        login_button_elem.click()
        self.assertIn('Feed | LinkedIn', self.browser.title)


    def dump_cookies(self):
        with open("cookies.pkl","wb") as file:
            pickle.dump(self.browser.get_cookies(), file)


    def upload_cookies(self):
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            self.browser.add_cookie(cookie)

