require 'eyes_selenium'
require 'selenium-webdriver'
require 'rest-client'

caps = Selenium::WebDriver::Remote::Capabilities.new

# choose some capabilities that will reflect
# the browser/os we want to test on.
caps['name'] = 'Applitools Example'
caps['browserName'] = 'Chrome'
caps['platform'] = 'Windows 10'
caps['screenResolution'] = '1366x768'
score = nil

# Initialize the eyes SDK and set your private API key.
eyes = Applitools::Selenium::Eyes.new
eyes.api_key = 'NOTMYAPIKEY'

username = "chase%40crossbrowsertesting.com"
authkey = "NOTMYAUTHKEY"

# setup a remote webdriver object for starting a session with CBT
driver = Selenium::WebDriver.for(:remote,
      :url => "http://#{username}:#{authkey}@hub.crossbrowsertesting.com:80/wd/hub",
      :desired_capabilities => caps)

begin
    # Start the test and set the browser's viewport size to 800x600.
    eyes.test(app_name: 'CrossBrowserTesting', test_name: 'My first Applitools test with Ruby',
            viewport_size: {width:800, height:600}, driver: driver) do

    # navigate to the webpage we'd like to visually test
    driver.get 'https://crossbrowsertesting.com/visual-testing'

    # Visual checkpoint
    eyes.check_window 'Visual Testing'

    score = 'pass'
  end
rescue Exception => ex
  puts 'Differences found by Applitools'
  score = 'fail'
ensure
  sessionId = driver.session_id
  response = RestClient.put("https://#{username}:#{authkey}@crossbrowsertesting.com/api/v3/selenium/#{sessionId}",
            "action=set_score&score=#{score}")
  
  # Close the browser.
  driver.quit
  # If the test was aborted before eyes.close was called, ends the test as aborted.
  eyes.abort_if_not_closed
end

