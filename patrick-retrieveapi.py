import urllib.request
import json
import pdb
import random

url = 'https://crossbrowsertesting.com/api/v3/selenium/browsers?format=json'
req = urllib.request.Request(url)

#This will be an object that will hold all variables and methods for a single CBT browser.def
class cbtObject:
	def __init__(self, cbtItem):
		self.api_name=cbtItem['api_name']
		self.device=cbtItem['device']
		self.device_type=cbtItem['device_type']
		self.name=cbtItem['name']
		self.version=cbtItem['version']
		self.type=cbtItem['type']
		self.icon_class=cbtItem['icon_class']
		self.upload_file_enabled=cbtItem['upload_file_enabled']

	#Returns a dictionary item with all properties matched to a value.
	def returnDict(self):
		return self.__dict__

cbtWindowsList = []
cbtMacList = []
cbtMobileList = []

##parsing response
r = urllib.request.urlopen(req).read()
parsedJson = json.loads(r.decode('utf-8'))

for dataPoint in parsedJson:
    	#Printing out now just for tracking. This will be removed for production.
		#print(dataPoint['api_name']," ",dataPoint['device']," ",dataPoint['name'])
		
		tempCBTObject = cbtObject(dataPoint)

		if tempCBTObject.device == 'mobile':
			cbtMobileList.append(tempCBTObject)
		elif tempCBTObject.type == 'Windows':
			cbtWindowsList.append(tempCBTObject)
		elif tempCBTObject.type == 'Mac':
			cbtMacList.append(tempCBTObject)



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


