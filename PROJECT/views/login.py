from PROJECT.settings import BROWSER, By, Keys, WebDriverWait, expected_conditions
from PROJECT.constant import WEBSITE_URL, USERNAME, PASSWORD, EMAIL


def login_account():
    BROWSER.get(WEBSITE_URL)
    
    try:
        elem_email = WebDriverWait(BROWSER, 10).until(
            expected_conditions.presence_of_element_located((By.NAME, "session_key"))
        )
        elem_email.send_keys(EMAIL)

        passowrd_elem = BROWSER.find_element(By.NAME, "session_password")
        passowrd_elem.send_keys(PASSWORD)

        login_button_elem = BROWSER.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
        BROWSER.implicitly_wait(2)
        login_button_elem.click()
        BROWSER.close()

    except Exception as e:
        BROWSER.quit()
