from selenium.common.exceptions import NoSuchElementException

class BasePage():
    # Конструктор с неявным ожиданием
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Метод для открытия страницы
    def open(self):
        self.browser.get(self.url)

    # Метод для проверки присутствия элемента
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True