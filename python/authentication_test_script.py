import unittest
from pages.loginPage import LoginPage
from config import selenium_driver

class AuthenticationTest(unittest.TestCase):

    def setUp(self):
        self.driver = selenium_driver.connect()

    def test_authentication(self):
        login = LoginPage(self.driver)
        login.now()
        self.assertTrue(self.driver.find_element_by_css_selector('#flash.success'))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
