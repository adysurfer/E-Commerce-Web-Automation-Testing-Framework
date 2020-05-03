import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.add_items_page import AddItems
from page_objects.checkout_page import CheckOutPage
from page_objects.home_page import HomePage
from test_data.get_excel_data import ExcelData
from utilities.base_class import BaseClass


# Get data from Excel for data driven execution for 'testcase 1'
@pytest.mark.parametrize("get_data", ExcelData.get_excel_dta("TC_1"))
# Test Case to test the complete product purchase functionality
class TestEnd2End(BaseClass):
    def test_end2end_purchase(self, get_data):

        log = self.get_logger()
        # creating an object of HomePage class
        home_page = HomePage(self.driver)
        # Creating an object of AddItems class
        add_items_page = AddItems(self.driver)
        # Creating an object of checkout_page
        checkout_page = CheckOutPage(self.driver)

        # get page title
        title = "Parallax Bag"
        log.info("Getting Page title")
        page_title = home_page.get_title()
        assert page_title == title

        # explicit wait is target at a specific object
        explicit_wait = WebDriverWait(self.driver, 8)
        explicit_wait.until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, "//div[@class='modal-body']/parent::div/parent::div/a"), "×"))

        # Close banner which appears after landing page has been loaded
        log.info("Closing the opening banner")
        home_page.get_close_banner()

        # select_item_style
        # Hover to navigation items using ActionChains class to choose an item

        log.info("Getting navigation items list")
        items = home_page.get_nav_items()

        for item in items:
            if item.text == "SHOES":
                log.info("Taking cursor to navigation where item is some item_name")
                self.perform_actions().move_to_element(item).perform()

                log.info("Getting navigation sub_items list where item is some item_name")
                sub_items = item.find_elements_by_css_selector("div ul li a")

                log.info("Selecting an item from sub_items")
                for it_sub in sub_items:
                    if "MEN'S SHOES" in it_sub.text:
                        # Click on sub_item if its present in the items list to get categories
                        it_sub.click()

                        # Scroll window to make an element appear on web page
                        log.info("Scrolling the window")
                        self.get_scroll_window()

                        # Add_items section
                        # Select an item
                        log.info("Get items list")
                        item_title = add_items_page.get_select_item()
                        for i in item_title:
                            if "Shoes Isabeal" in i.text:
                                i.click()
                                break

                        break
                break
            else:
                log.error("Wrong Item")

        # add_size
        log.info("Selecting size")
        radio_btn_size = add_items_page.get_size_list()

        add_size = radio_btn_size[7]

        # select size
        add_size.click()
        log.info("Select color")
        # add color
        radio_btn_color = add_items_page.get_color()
        add_color = radio_btn_color[11]

        # select color
        add_color.click()

        # Scroll window to make an element appear and clickable on web page
        log.info("Scrolling the window")
        self.get_scroll_window()

        # add  to cart
        log.info("Adding to cart")
        add_items_page.get_add_to_cart()

        explicit_wait.until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "section[class='previewCartCheckout']")))

        log.info("Proceeding to checkout page")
        # proceed to checkout
        add_items_page.get_proceed_to_checkout()

        explicit_wait.until(
            expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "label[for='email']"), "Email "
                                                                                                       "Address"))

        # Checkout page form
        log.info("Enter Email")
        checkout_page.get_email(get_data["email"])

        log.info("Check Subscribe checkbox")
        subscribe = checkout_page.get_subscribe()
        subscribe.click()

        is_subscribed = subscribe.find_element_by_xpath('input')
        # check if the subscribe checkbox is selected
        assert is_subscribed.get_attribute("value") == "true"

        # click to go to shipping details
        log.info("Go to shipping section")
        checkout_page.get_shipping_section()

        explicit_wait.until(expected_conditions.text_to_be_present_in_element((By.ID, "countryCodeInput"),
                                                                              get_data["country"]))

        log.info("Choose country from static dropdown")
        # continue shipping details, select country
        self.get_dropdown_by_text(checkout_page.get_country(), get_data["country"])

        assert checkout_page.get_country().get_attribute("value") == get_data["country_value"]

        # firstName
        log.info("Get First Name")
        checkout_page.get_first_name(get_data["first_name"])

        # lastName
        log.info("get last name")
        checkout_page.get_last_name(get_data["last_name"])

        # Address Line 1
        log.info("Get address_line1")
        checkout_page.get_address_line1(get_data["address_line1"])

        # Address Line 2
        log.info(f"Data received for address_line2 is {get_data['address_line2']}")
        checkout_page.get_address_line2(get_data["address_line2"])

        # City
        log.info("get city")

        checkout_page.get_city(get_data['city'])

        # postal Code
        log.info("get postal code")
        checkout_page.get_postal_code(get_data["postal_code"])

        # Phone
        log.info("get phone")
        checkout_page.get_phone(get_data["phone_number"])

        # Billing address checkbox selected as default
        log.info("get billing address")
        check_billing = checkout_page.get_check_billing_address()
        is_check_billing = check_billing.find_element_by_xpath("input")

        assert is_check_billing.get_attribute("value") == "true"

        # Comments in order
        log.info("get comments on order")
        checkout_page.get_comments(get_data["comments"])

        explicit_wait.until(expected_conditions.element_to_be_clickable((By.ID, "checkout-shipping-continue")))

        # continue to payment by button

        log.info("continue to payment from here")
        checkout_page.get_continue_to_payment()

        explicit_wait.until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, "//span[text()='Check']"), "Check"))

        # Select payment options radio btn
        log.info("Choose Payment Option")
        pay_options = checkout_page.get_payment_options()

        for p in pay_options:

            if p.get_attribute("for") == "radio-cod":
                p.click()
                break

        # Place Order
        log.info("Place your Order Button")
        checkout_page.get_place_your_order()

        explicit_wait.until(
            expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "optimizedCheckout-headingPrimary"),
                                                              "Thank you"))

        # Confirmation text check
        log.info("Checking confirmation text matches the required text")
        required_text = "Thank you"
        confirmation_text = checkout_page.get_confirmation_text().text
        log.info(f"Confirmation text is {confirmation_text}")
        assert required_text in confirmation_text
