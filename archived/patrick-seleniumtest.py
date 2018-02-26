import unittest
from selenium import webdriver
import requests

class SeleniumCBT(unittest.TestCase):
    def setUp(self):

        self.username = "patrick@theparkisons.com"
        self.authkey  = "u70ee7e205f04560"

        self.api_session = requests.Session()
        self.api_session.auth = (self.username,self.authkey)
        self.test_result = None

        caps = {}
        caps['name'] = 'Basic Test Example'
        caps['build'] = '1.0'
        caps['browserName'] = 'Chrome'
        caps['deviceName'] = 'Nexus 9'
        caps['platformVersion'] = '6.0'
        caps['platformName'] = 'Android'
        caps['deviceOrientation'] = 'portrait'

        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username,self.authkey)
        )

        self.driver.implicitly_wait(20)

    '''def test_CBT(self):
            self.driver.get('http://crossbrowsertesting.github.io/selenium_example_page.html')
            self.assertEqual("Selenium Test Example Page", self.driver.title)
            self.test_result = 'pass'
            self.driver.quit()'''

    def test_CBT(self):
            self.driver.get('http://local:8000/index.html')
            self.assertEqual("Hello CBT World!", self.driver.title)
            self.test_result = 'pass'
            self.driver.quit()     

if __name__ == '__main__':
    unittest.main()