from basePage import BasePage

class LoginPage(BasePage):

    login_form            = '#login'
    input_username        = '#username'
    input_password        = '#password'
    notification_message  = '#flash'

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('http://the-internet.herokuapp.com/login')
        self.assertTrue(self.driver.find_element_by_css_selector(self.login_form))

    def submit(self):
        self.driver.find_element_by_css_selector(self.input_username).send_keys("username")
        self.driver.find_element_by_css_selector(self.input_password).send_keys("password")
        self.driver.find_element_by_css_selector(self.login_form).submit()
        self._wait_for(self.notification_message)
