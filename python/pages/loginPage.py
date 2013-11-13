from basePage import BasePage

class LoginPage(BasePage):

    login_form            = '#login'
    input_username        = '#username'
    input_password        = '#password'
    notification_message  = '#flash'

    def __init__(self, driver):
        self.driver = driver
        self._visit('http://the-internet.herokuapp.com/login')
        self.assertTrue(self.driver.find_element_by_css_selector(self.login_form))

    def now(self):
        self._type(self.input_username, "username")
        self._type(self.input_password, "password")
        self._submit(self.login_form)
        self._wait_for(self.notification_message)
