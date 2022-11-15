from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BUTTON)
        button.click()

    def should_be_add_message(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BUSKET_MESSAGE), "Missing message to add item to cart"

    def should_be_product_match(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_ADD_TO_BUSKET_MESSAGE).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text, "The product added to the cart does not match the product"

    def should_be_cost_match(self):
        assert self.browser.find_element(
            *ProductPageLocators.COST_BASKET).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text, "The product added to the cart does not match the product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BUSKET_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_BUSKET_MESSAGE), \
            "Success message didn't go away, but it should"
