from selenium import webdriver

class SeleniumWrapper:

  def connect(self):
    self.driver = webdriver.Firefox()

    return self.driver
