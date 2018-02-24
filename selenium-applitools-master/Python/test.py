from selenium import webdriver
from applitools.eyes import Eyes, DiffsFoundError
import requests

username = 'patrick@theparkisons.com'
authkey = 'u70ee7e205f04560'
test_result = None
eyes = Eyes()

# Initialize the eyes SDK and set your private API key.
eyes.api_key = 'NOTMYAPIKEY'

try:
    # choose some capabilities that will reflect
    # the browser/os we want to test on. 
    caps = {
        'name': 'Applitools Example',
        'browserName': 'Chrome',
        'platform': 'Windows 10',
        'screenResolution': '1366x768'
    }

    # open a remote webdriver connected to cbt's hub
    driver = webdriver.Remote(
        desired_capabilities=caps,
        command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(username,authkey)
    )

    # Start the test and set the browser's viewport size to 800x600.
    eyes.open(driver=driver, app_name='CrossBrowserTesting', test_name='My first Applitools test with Python!',
    	viewport_size={'width': 800, 'height': 600})
    
    # We want to take a full page screenshot
    eyes.force_full_page_screenshot = True
    
    driver.get('https://crossbrowsertesting.com/visual-testing')

    # Visual checkpoint
    eyes.check_window('Visual Testing')

    # End the test.
    eyes.close()
    test_result = 'pass'

except DiffsFoundError as e:
    # if differences are found, eyes will throw a DiffsFoundError
    # we'll set the test score on CBT's side to match up
    test_result = 'fail'

finally:
    # make an API call to CrossBrowserTesting set the score
    requests.put('https://crossbrowsertesting.com/api/v3/selenium/' + driver.session_id, 
        data={ "action": "set_score", "score": "pass" }, auth=(username,authkey))
        
    # Close the browser.
    driver.quit()

    # If the test was aborted before eyes.close was called, ends the test as aborted.
    eyes.abort_if_not_closed()