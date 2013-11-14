RSpec.configure do |config|
  config.before(:all) do
    $base_url = 'http://the-internet.herokuap.com'
  end

  config.before(:each) do
    @driver = Selenium::WebDriver.for :firefox
  end

  config.after(:each) do
    @driver.quit
  end
end
