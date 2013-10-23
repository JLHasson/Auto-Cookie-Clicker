#Auto Cookie script
#Written by Lance Hasson and Je Hon Tan
#Uses Splinter API found at http://splinter.cobrateam.info/

from splinter import Browser

#object to be clicked
cookie = browser.find_by_id('bigCookie')
#holds ["name", amount owned, base c']
buildings = {
	"curser": [0, 0.1],
	"grandma": [0, 0.5],
	"farm": [0, 4],
	"factory": [0, 10],
	"mine": [0, 40],
	"shipment": [0, 100],
	"alchemy": [0, 400],
	"portal": [0, 6666],
	"time": [0, 98765],
	"antimatter": [0, 999999]
}

def main ():
	startBrowser() #Create browsing session
	while True:
		cookie.click()
		purchaseUpgrade(pageSource)		

def startBrowser():
	browser = Browser('chrome')
	browser.visit('http://orteil.dashnet.org/cookieclicker/')

def whichUpgrade():
	"""
	This function will calculate which upgrade to be purchased next between
	two values.
	It will use the function y = (dc'/x)(ta/tb), where y is the return value
	of the purchase, dc is change in cookies/second after purchase, x is the
	cost of the upgrade, ta and tb are the time is takes to save up for each
	upgrade respectively. T will be calculated using the formula T = (x/c')
	where x is the cost of the upgrade and c' is the current cookies per second.
	
	Returns id of next upgrade to purchase, and cost of that purchase.
	"""
	upgradeReturns = []
	for i in range(0, 9):
		currentReturn = calcReturn(i)
		upgradeReturns = upgradeReturns + currentReturn[]

def purchaseUpgrade(upgrade, cost):
	"""
	This function will perform the action of purchasing the next upgrade. 
	It will take the returned value from whichUpgrade() as two parameters
	with which it will take the current amount of cookies, and check if 
	you have enough to purchase the next upgrade, if not exit, if so
	purchase it and then rerun whichUpgrade(). After the purchase of a
	building it will +1 the count stored in the buildings variable.
	"""
	
	

	whichUpgrade()

def calcReturn(upgradeId):
	# Grabbing all needed elements off page based on current upgrade
	nextUpgrade = upgradeId++
	productId = "product" + str(upgradeId)
	nextProductId = "product" + str(nextUpgrade)
	currentProductPrice = find_by_xpath('//*[@id="' + productId + '"]/div[2]/span"')
	nextProductPrice = find_by_xpath('"//*[@id="' + nextProductId + '"]/div[2]/span"')
	currentCPSstring = find_by_xpath('//*[@id="cookies"]/div') # Returns "per second : ___"
	currentCPS = currentCPSstring.split() # Split returned string
	currentCPS = float(currentCPS[13:])	# Retrieve only numbers at the end of the string and convert to float
		

def getCPS (): # Alternative to above method
	"""
	The advantage of this method to the other is that in this method
	the current CPS is stored in memory rather than having to scrap
	the page each time you need the current CPS. This adds efficiency
	to the program.
	"""
	totalCPS = ((buildings["curser"][0] * buildings["curser"][1]) + (buildings["grandma"][0] * buildings["grandma"][1]) + (buildings["farm"][0] * buildings["farm"][1]) + (buildings["factory"][0] * buildings["factory"][1]) + (buildings["mine"][0] * buildings["mine"][1]) + (buildings["shipment"][0] * buildings["shipment"][1]) + (buildings["alchemy"][0] * buildings["alchemy"][1]) + (buildings["portal"][0] * buildings["portal"][1]) + (buildings["time"][0] * buildings["time"][1]) + (buildings["antimatter"][0] * buildings["antimatter"][1]))
