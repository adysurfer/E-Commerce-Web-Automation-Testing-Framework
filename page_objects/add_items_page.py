from selenium.webdriver.common.by import By


class AddItems:
    select_item = (By.CSS_SELECTOR, "h4[class='card-title'] a")
    size_list = (By.CSS_SELECTOR, ".form-field:nth-child(1) label")
    color_list = (By.XPATH, "//div[2]//label")
    add_to_cart = (By.CSS_SELECTOR, "input[id='form-action-addToCart']")
    proceed_to_checkout = (By.CSS_SELECTOR, "section[class='previewCartCheckout'] a:nth-child(1)")

    def __init__(self, driver):
        self.driver = driver

    def get_select_item(self):
        get_select_items = self.driver.find_elements(*AddItems.select_item)
        return get_select_items

    def get_size_list(self):
        list = self.driver.find_elements(*AddItems.size_list)
        return list

    def get_color(self):
        color = self.driver.find_elements(*AddItems.color_list)
        return color

    def get_add_to_cart(self):
        self.driver.find_element(*AddItems.add_to_cart).click()

    def get_proceed_to_checkout(self):
        self.driver.find_element(*AddItems.proceed_to_checkout).click()
