from basePage import BasePage
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('http://the-internet.herokuapp.com/login')
        self.assertTrue(self.driver.find_element_by_css_selector('#login'))

    def _element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def _wait_for(self, locator):
        WebDriverWait(self.driver, 5).until(lambda driver : self._element_present('css', locator))

    def submit(self):
        self.driver.find_element_by_css_selector('#username').send_keys("username")
        self.driver.find_element_by_css_selector('#password').send_keys("password")
        self.driver.find_element_by_css_selector('#login').submit()
        self._wait_for('#flash')
