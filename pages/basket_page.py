from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_empty(self):
        self.should_be_no_products_in_basket()
        self.should_be_basket_empty_text()

    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "BASKET_ITEM is presented, but should not be"

    def should_be_basket_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_TEXT), "Basket text is not presented"
