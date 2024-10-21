from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")  # Кнопка "Добавить в корзину"
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")  # Сообщение о добавлении товара
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")  # Название продукта
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")  # Цена продукта
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini")  # Общая сумма корзины

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini .btn-default")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
