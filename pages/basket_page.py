from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "There must be no products in the basket"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "There is no message that your basket is empty"