from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()  # Открываем главную страницу
    page.go_to_login_page()  # Переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)  # Явная инициализация страницы логина
    login_page.should_be_login_page()  # Проверяем, что это действительно страница логина
    
def test_guest_can_add_product_to_basket(browser):
    # Указываем ссылку на страницу с продуктом и промо-акцией
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    
    # Инициализируем страницу продукта
    page = ProductPage(browser, link)
    
    # Открываем страницу продукта
    page.open()
    
    # Добавляем товар в корзину
    page.add_to_basket()
    
    # Решаем математическую задачу и подтверждаем
    page.solve_quiz_and_get_code()
    
    # Проверяем, что появилось сообщение о добавлении товара в корзину
    page.should_be_success_message()
    
    # Проверяем, что сумма корзины соответствует цене товара
    page.should_be_basket_total()