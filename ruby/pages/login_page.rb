require_relative 'base_page'

module Pages
  class Login < BasePage

    LOGIN_FORM            = '#login'
    INPUT_USERNAME        = '#username'
    INPUT_PASSWORD        = '#password'
    NOTIFICATION_MESSAGE  = '#flash'
    SUCCESS_MESSAGE       = '#flash.success'

    attr_writer :username, :password

    def initialize(driver)
      super
      visit('/login')
      find(LOGIN_FORM).should be_true
    end

    def now
      type(INPUT_USERNAME, username)
      type(INPUT_PASSWORD, password)
      submit(LOGIN_FORM)
      wait_for(NOTIFICATION_MESSAGE)
    end

    def success_message_present?
      element_present?(SUCCESS_MESSAGE)
    end

  end
end
