import pytest
from .pages.product_page import ProductPage

@pytest.mark.login
class TestLoginFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        # В реальном проекте можно было бы создать товар через API
        # self.product = ProductFactory(title="Best book created by robot")
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        yield
        # После выполнения теста можно было бы удалить данные
        # self.product.delete()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_login_link()
