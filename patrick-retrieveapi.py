import urllib.request
import json
import pdb
import random

url = 'https://crossbrowsertesting.com/api/v3/selenium/browsers?format=json'
req = urllib.request.Request(url)

#This will be an object that will hold all variables and methods for a single CBT browser.def
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

cbtWindowsList = []
cbtMacList = []
cbtMobileList = []

##parsing response
r = urllib.request.urlopen(req).read()
parsedJson = json.loads(r.decode('utf-8'))

#Iterate through each browser type and resolution for each device.
#Add the unique device to the list for the device type.

for dataPoint in parsedJson:
	tempCBTObject = cbtObject(dataPoint)
	browserCounter = 0
	resolutionCounter = 0
	
	#Printing out now just for tracking. This will be removed for production.
	#print(dataPoint['api_name']," ",dataPoint['device']," ",dataPoint['name'])

	#Iterating through the browsers.
	#cbtItem['browsers'][x]['caps']['browserName']

	for browserItem in dataPoint['browsers']:
		for r in dataPoint['resolutions']:
    		#Assign vales to the cbtObject.
			tempCBTObject = cbtObject(dataPoint)
			tempCBTObject.name = 'Basic test example.'
			tempCBTObject.build = '1.0'
			tempCBTObject.browserName = dataPoint['browsers'][browserCounter]['caps']['browserName']

			#Determines if mobile or desktop.
			if dataPoint['device'] == 'mobile':
				tempCBTObject.deviceName = dataPoint['caps']['deviceName']
				tempCBTObject.version = dataPoint['caps']['platformVersion']
				tempCBTObject.platform = dataPoint['caps']['platformName']
				tempCBTObject.deviceOrientation = dataPoint['resolutions'][resolutionCounter]['orientation']
				tempCBTObject.screenResolution = dataPoint['resolutions'][resolutionCounter]['name']

			#Add the completed CBTObject to the appropriate list
			if dataPoint['device'] == 'mobile':
				cbtMobileList.append(tempCBTObject)
			elif tempCBTObject.type == 'Windows':
				cbtWindowsList.append(tempCBTObject)
			elif tempCBTObject.type == 'Mac':
				cbtMacList.append(tempCBTObject)
			


			
			
			#Increment the resolution counters to go onto the next CBTObject
			resolutionCounter += 1
			pdb.set_trace()
		
		#Increment the browser Counter to go on to the next cbtObject
		browserCounter += 1




#Get the random list indexes for the 3 types of devices to scan: windows, mac, mobile
macIndex = random.randrange(len(cbtMacList))
mobileIndex = random.randrange(len(cbtMobileList))
windowsIndex = random.randrange(len(cbtWindowsList))

#Retrive the cbtObject from each list.cbtMobileList
print("Mac: ",cbtMacList[macIndex].name)
print("Mobile: ",cbtMobileList[mobileIndex].name)
print("Windows: ",cbtWindowsList[windowsIndex].name)
#pdb.set_trace()

counter = 0


