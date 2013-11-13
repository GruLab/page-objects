import unittest
from pages.loginPage import LoginPage
from setup import driver

class AuthenticationTest(unittest.TestCase):

    def setUp(self):
        self.driver = driver.connect()

    def test_authentication(self):
        login = LoginPage(self.driver)
        login.username = 'username'
        login.password = 'password'
        login.now()
        self.assertTrue(login.success_message_present())

    def tearDown(self):
        driver.close()

if __name__ == "__main__":
    unittest.main()
