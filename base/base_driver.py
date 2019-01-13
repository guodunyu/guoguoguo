from selenium import webdriver


def init_driver():
    driver = webdriver.Firefox()
    driver.get("http://localhost:800/iwebshop/")
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver


if __name__ == '__main__':
    init_driver()