import json
import pdb
import random
import requests
from selenium import webdriver
import unittest
import urllib.request

ut = unittest.TestCase

#This will be an object that will hold all variables and
#methods for a single CBT browser.
class cbtObject:
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
            tempCBTObject.name = 'Basic test example.'
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
                tempCBTObject.version = dataPoint['browsers'][browserCounter]['version']
                tempCBTObject.platform = dataPoint['caps']['platform']
                tempCBTObject.screenResolution = dataPoint['resolutions'][resolutionCounter]['name'] 
			
			#Mac detected
            elif dataPoint['type'] == 'Mac':
                tempCBTObject.version = dataPoint['browsers'][browserCounter]['version']
                tempCBTObject.platform = dataPoint['caps']['platform']
                tempCBTObject.screenResolution = dataPoint['resolutions'][resolutionCounter]['name'] 

			#Add the completed CBTObject to the appropriate list
            if dataPoint['device'] == 'mobile':
                cbtMobileList.append(tempCBTObject)
            elif dataPoint['type'] == 'Windows':
                cbtWindowsList.append(tempCBTObject)
            elif dataPoint['type'] == 'Mac':
                cbtMacList.append(tempCBTObject)

                #Increment the resolution counters to go onto the next CBTObject
                resolutionCounter += 1
		
        #Increment the browser Counter to go on to the next cbtObject
        browserCounter += 1
		#Reset the resolution counter to zero for start of new browser.
        resolutionCounter = 0

#Get the random list indexes for the 3 types of devices to scan: windows, mac, mobile
macIndex = random.randrange(len(cbtMacList))
mobileIndex = random.randrange(len(cbtMobileList))
windowsIndex = random.randrange(len(cbtWindowsList))

#Retrive the cbtObject from each list.cbtMobileList.
#This is used for user feedback.
print("Mac: Count", 
	    len(cbtMacList), ": ",
	    cbtMacList[macIndex].platform
    )
print("Mobile: Count",
    len(cbtMobileList), ": ",
    cbtMobileList[mobileIndex].platform
    )

print("Windows: Count",
    len(cbtWindowsList),
	": ",
	cbtWindowsList[windowsIndex].platform)


counter = 0
