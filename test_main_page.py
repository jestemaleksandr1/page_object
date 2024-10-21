from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()  # Открываем главную страницу
    page.go_to_login_page()  # Переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)  # Явная инициализация страницы логина
    login_page.should_be_login_page()  # Проверяем, что это действительно страница логина