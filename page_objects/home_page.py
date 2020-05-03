from selenium.webdriver.common.by import By


class HomePage:
    # class variable

    close_banner = (By.XPATH, "//div[@class='modal-body']/parent::div/parent::div/a")
    navigation_items = (By.CSS_SELECTOR,"li[class='navPages-item']")

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        page_title = self.driver.title
        return page_title

    # * treats variable as tuple, and deserialize it
    def get_close_banner(self):
        self.driver.find_element(*HomePage.close_banner).click()

    def get_nav_items(self):
        items = self.driver.find_elements(*HomePage.navigation_items)
        return items

