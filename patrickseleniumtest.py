import json
import pdb
import random
import requests
from selenium import webdriver
import unittest
import urllib.request

#This object will represent a browsed computer/device and browser combination.
class cbtObject:
    #All properties are initialized to empty strings.
    def __init__(self, cbtItem):
        self.name = ''
        self.build = '1.0'
        self.browserName = ''
        self.deviceName = ''
        self.version = ''
        self.platform = ''
        self.deviceOrientation = ''
        self.screenResolution = ''

	#Returns a dictionary item with all properties matched to a value.
    def returnDict(self):
        return self.__dict__

#This class will intialize and launch the three unit test. The source for this was located in the CBT help docs.
class SeleniumCBT(unittest.TestCase):
    
    #These are the three list that hold the Windows, Mac, and Mobile browsers.
    cbtWindowsList = []
    cbtMacList = []
    cbtMobileList = []

    #retrieve a collection of all available browsers.
    url = 'https://crossbrowsertesting.com/api/v3/selenium/browsers?format=json'
    req = urllib.request.Request(url)

    ##parsing response
    r = urllib.request.urlopen(req).read()
    parsedJson = json.loads(r.decode('utf-8'))

    #Iterate through each browser type and resolution for each device.
    #Add the unique device to the list for the device type.
    for dataPoint in parsedJson:
        tempCBTObject = cbtObject(dataPoint)
        browserCounter = 0
        resolutionCounter = 0

        #Iterating through the browsers.
        for browserItem in dataPoint['browsers']:
            for r in dataPoint['resolutions']:
                #Assign vales to the cbtObject.
                tempCBTObject = cbtObject(dataPoint)
                tempCBTObject.name = 'Basic test example.' #Over written later.
                tempCBTObject.build = '1.0'
                tempCBTObject.browserName = (
                    dataPoint['browsers'][browserCounter]['caps']['browserName']
                )
                #Determines if mobile or desktop.

                #Mobile detected.
                if dataPoint['device'] == 'mobile':
                    tempCBTObject.deviceName = dataPoint['caps']['deviceName']
                    tempCBTObject.version = dataPoint['caps']['platformVersion']
                    tempCBTObject.platform = dataPoint['caps']['platformName']
                    tempCBTObject.deviceOrientation = (
                        dataPoint['resolutions'][resolutionCounter]['orientation']
                    )
                
                #Windows detected
                elif dataPoint['type'] == 'Windows':
                    tempCBTObject.deviceName = dataPoint['name']
                    tempCBTObject.version = dataPoint['browsers'][browserCounter]['version']
                    tempCBTObject.platform = dataPoint['caps']['platform']
                    tempCBTObject.screenResolution = dataPoint['resolutions'][resolutionCounter]['name'] 
                
                #Mac detected
                elif dataPoint['type'] == 'Mac':
                    tempCBTObject.deviceName = dataPoint['name']
                    tempCBTObject.version = dataPoint['browsers'][browserCounter]['version']
                    tempCBTObject.platform = dataPoint['caps']['platform']
                    tempCBTObject.screenResolution = dataPoint['resolutions'][resolutionCounter]['name'] 

                #Add the completed CBTObject to the appropriate list
                if dataPoint['device'] == 'mobile':
                    cbtMobileList.append(tempCBTObject)
                elif dataPoint['type'] == 'Windows':
                    cbtWindowsList.append(tempCBTObject)
                    #Increment the resolution counters to go onto the next CBTObject
                    resolutionCounter += 1
                elif dataPoint['type'] == 'Mac':
                    cbtMacList.append(tempCBTObject)
                    #Increment the resolution counters to go onto the next CBTObject
                    resolutionCounter += 1
            
            #Increment the browser Counter to go on to the next cbtObject
            browserCounter += 1
            #Reset the resolution counter to zero for start of new browser.
            resolutionCounter = 0

    #Testing setkup
    def setUp(self):

        self.username = "patrick@theparkisons.com"
        self.authkey  = "u70ee7e205f04560"

        self.api_session = requests.Session()
        self.api_session.auth = (self.username,self.authkey)
        self.test_result = None
        

    #Test a Windows device.
    def test_CBTWindows(self):
        
        #retrieve a random windows list object.
        #Get the random list indexes for the Windows device to scan.
        windowsIndex = random.randrange(len(self.cbtWindowsList))
        tempItem = self.cbtWindowsList[windowsIndex]

        #Print test item for user feed back after the test.
        print("Windows Test: Tested '",
            tempItem.deviceName.strip(),
            "' with a",
            tempItem.browserName.strip(),
            "browser(",tempItem.screenResolution.strip()
            ,")."
        )           
        caps={}
        caps['name'] = 'Windows Test Example'
        caps['build'] = tempItem.build
        caps['browserName'] = tempItem.browserName
        caps['platformVersion'] = tempItem.version
        caps['platformName'] = tempItem.platform
        caps['screenResolution'] = tempItem.screenResolution

        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username,self.authkey)
        )

        self.driver.implicitly_wait(20)
        self.driver.get('http://local:8000/index.html')
        self.assertEqual("Hello CBT World!", self.driver.title)
        self.test_result = 'pass'
        self.driver.quit()
        
    #Test a Mac device.
    def test_CBTMac(self):
        #Get the random list indexes for the Mac device to scan.
        macIndex = random.randrange(len(self.cbtMacList))
        tempItem = self.cbtMacList[macIndex]

        #Print test item for user feed back after the test.
        print("Mac Test: Tested '",tempItem.deviceName,"' with a ",tempItem.browserName," browser(",tempItem.screenResolution,").")        
        caps={}
        caps['name'] = 'Mac Test Example'
        caps['build'] = tempItem.build
        caps['browserName'] = tempItem.browserName
        caps['platformVersion'] = tempItem.version
        caps['platformName'] = tempItem.platform
        caps['screenResolution'] = tempItem.screenResolution

        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username,self.authkey)
        )
        self.driver.implicitly_wait(20)
        self.driver.get('http://local:8000/index.html')
        self.assertEqual("Hello CBT World!", self.driver.title)
        self.test_result = 'pass'
        self.driver.quit()

    #Test a mobile device.
    def test_CBTMobile(self):
        
        #Get the random list indexes for the Mobile device to scan.
        mobileIndex = random.randrange(len(self.cbtMobileList))
        tempItem = self.cbtMobileList[mobileIndex]

        #Print test item for user feed back after the test.
        print("Mobile Test: Tested '",tempItem.deviceName,"' with a ",tempItem.browserName," browser(",tempItem.deviceOrientation,").")
        caps={}
        caps['name'] = 'Mobile Test Example'
        caps['build'] = tempItem.build
        caps['browserName'] = tempItem.browserName
        caps['deviceName'] = tempItem.deviceName
        caps['platformVersion'] = tempItem.version
        caps['platformName'] = tempItem.platform
        caps['deviceOrientation'] = tempItem.deviceOrientation

        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username,self.authkey)
        )
        self.driver.implicitly_wait(20)
        self.driver.get('http://local:8000/index.html')
        self.assertEqual("Hello CBT World!", self.driver.title)
        self.test_result = 'pass'
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()