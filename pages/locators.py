from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    CART_LINK = (By.CSS_SELECTOR, '.btn-group > a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    ALERT_SUCCESS_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-success > div > strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    BASKET_PRICE = (By.CSS_SELECTOR, '.basket-mini')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')

class BasketPageLocators():
    BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_ITEM = (By.CSS_SELECTOR, '.basket-items')
