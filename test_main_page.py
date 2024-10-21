from .pages.main_page import MainPage

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # Инициализация объекта страницы
    page.open()  # Открытие главной страницы
    page.should_be_login_link()  # Проверка наличия ссылки на логин
