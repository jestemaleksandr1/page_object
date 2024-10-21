from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")  # Кнопка "Добавить в корзину"
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")  # Сообщение о добавлении товара
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")  # Название продукта
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")  # Цена продукта
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini")  # Общая сумма корзины

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")