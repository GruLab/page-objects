module Pages
  class BasePage

    attr_reader :driver

    def initialize(driver)
      @driver = driver
    end

    def element_present?(locator)
      begin
        find(locator)
      rescue NoSuchElementException
        false
      end
    end

    def wait_for(locator)
      Selenium::WebDriver::Wait.new(:timeout => 5).until { element_present?(locator) }
    end

    def find(locator)
      driver.find_element(css: locator)
    end

    def type(locator, text)
      find(locator).send_keys(text)
    end

    def submit(locator)
      find(locator).submit
    end

    def visit(url_path)
      driver.get(base_url + url_path)
    end

  end
end
