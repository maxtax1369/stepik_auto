from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_be_product_add_to_cart(self):
        self.should_be_message_product_add_to_cart()
        self.should_be_basket_price_equal_added_product()

    def should_be_message_product_add_to_cart(self):
        product_name_text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        success_alerts = self.browser.find_elements(*ProductPageLocators.ALERT_SUCCESS_PRODUCT_NAME)

        is_match = False
        alert_text_list = []
        for success_alert in success_alerts:
            alert_text = success_alert.text
            alert_text_list.append(alert_text)
            if product_name_text == alert_text:
                is_match = True
                break

        assert is_match, f'Product name "{product_name_text}" is not equal to "{alert_text_list}"'

    def should_be_basket_price_equal_added_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

        assert product_price in basket_price, f'Product price "{product_price}" is not contains basket price "{basket_price}"'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "The success message does not disappear"
