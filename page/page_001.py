from selenium.webdriver.common.by import By

from base.base_action import Base_Action

from base.base_read import readfile
class Page_001(Base_Action):
    sign_button = By.LINK_TEXT, "登录"
    user_button = By.CSS_SELECTOR, "[type='text']"
    password_button = By.CSS_SELECTOR, "[type='password']"
    signin_button = By.CSS_SELECTOR, ".submit_login"
    assert_button = By.CSS_SELECTOR, ".prompt"

    def __init__(self, driver):
        Base_Action.__init__(self, driver)

    def click_sign(self):
        self.click(self.sign_button)

    def send_user(self,text):
        self.send_keys(self.user_button, text)

    def send_password(self, text):
        self.send_keys(self.password_button, text)

    def click_sign_in(self):
        self.click(self.signin_button)

    def is_text(self, message, num):
        try:
            self.find_text(message)
            return True
        except Exception:
            self.driver.get_screenshot_as_file("./screen/" + num +"image.jpg")
            return False



