require_relative 'pages/login_page'

describe 'Authentication' do

  let(:login) { Pages::Login.new(@driver) }

  it 'success' do
    login.username = 'username'
    login.password = 'password'
    login.now
    login.success_message_present?.should be_true
  end

end
