from basePage import BasePage
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class LoginPage(BasePage):

    login_form            = '#login'
    input_username        = '#username'
    input_password        = '#password'
    notification_message  = '#flash'

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('http://the-internet.herokuapp.com/login')
        self.assertTrue(self.driver.find_element_by_css_selector(self.login_form))

    def _element_present(self, locator):
        try:
            self.driver.find_element_by_css_selector(locator)
        except NoSuchElementException, e: return False
        return True

    def _wait_for(self, locator):
        WebDriverWait(self.driver, 5).until(lambda driver : self._element_present(locator))

    def submit(self):
        self.driver.find_element_by_css_selector(self.input_username).send_keys("username")
        self.driver.find_element_by_css_selector(self.input_password).send_keys("password")
        self.driver.find_element_by_css_selector(self.login_form).submit()
        self._wait_for(self.notification_message)
