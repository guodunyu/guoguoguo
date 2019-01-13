from selenium.webdriver.common.by import By


class Base_Action():

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        self.find_element(loc).click()

    def send_keys(self, loc, text):

        self.find_element(loc).send_keys(text)

    def find_text(self, message):

        return self.driver.find_element(By.XPATH, "//*[text()='" + message + "']")

    def find_element(self, loc):
        return self.driver.find_element(loc[0], loc[1])

