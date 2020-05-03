class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    def get_email(self, email):
        self.driver.find_element_by_id('email').send_keys(email)

    def get_subscribe(self):
        subscribe = self.driver.find_element_by_xpath("//input[@id='shouldSubscribe']/parent::div")
        return subscribe

    def get_shipping_section(self):
        self.driver.find_element_by_css_selector("#checkout-customer-continue").click()

    def get_country(self):
        country = self.driver.find_element_by_id("countryCodeInput")
        return country

    def get_first_name(self, first_name):
        self.driver.find_element_by_id("firstNameInput").send_keys(first_name)

    def get_last_name(self, last_name):
        self.driver.find_element_by_id("lastNameInput").send_keys(last_name)

    def get_address_line1(self, address_line1):
        self.driver.find_element_by_id("addressLine1Input").send_keys(address_line1)

    def get_address_line2(self, address_line2):
        self.driver.find_element_by_id("addressLine2Input").send_keys(address_line2)

    def get_city(self, city):
        self.driver.find_element_by_id("cityInput").send_keys(city)

    def get_postal_code(self, postal_code):
        self.driver.find_element_by_id("postCodeInput").send_keys(postal_code)

    def get_phone(self, phone):
        self.driver.find_element_by_id("phoneInput").send_keys(phone)

    def get_check_billing_address(self):
        billing = self.driver.find_element_by_xpath("//label[@for='sameAsBilling']//parent::div")
        return billing

    def get_comments(self, comments):
        self.driver.find_element_by_css_selector("input[name='orderComment']").send_keys(comments)

    def get_continue_to_payment(self):
        self.driver.find_element_by_id("checkout-shipping-continue").click()

    def get_payment_options(self):
        po = self.driver.find_elements_by_xpath("//div[@class='form-body']/ul/li/div/div/label")
        return po

    def get_place_your_order(self):
        self.driver.find_element_by_id("checkout-payment-continue").click()

    def get_confirmation_text(self):
        ct = self.driver.find_element_by_class_name("optimizedCheckout-headingPrimary")
        return ct

