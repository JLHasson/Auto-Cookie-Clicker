#Auto Cookie script
#Written by Lance Hasson and Je Hon Tan
#Uses Splinter API found at http://splinter.cobrateam.info/

from splinter import Browser
from bs4 import BeautifulSoup
import urllib2

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
	pageSource = getPageData()  #Get data of the page
	while True:
		cookie.click()
		purchaseUpgrade(pageSource)		

def startBrowser():
	browser = Browser('chrome')
	browser.visit('http://orteil.dashnet.org/cookieclicker/')

def whichUpgrade(pageSource):
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
	
	

def purchaseUpgrade(upgrade, cost, pageSource):
	"""
	This function will perform the action of purchasing the next upgrade. 
	It will take the returned value from whichUpgrade() as two parameters
	with which it will take the current amount of cookies, and check if 
	you have enough to purchase the next upgrade, if not exit, if so
	purchase it and then rerun whichUpgrade(). After the purchase of a
	building it will +1 the count stored in the buildings variable.
	"""
	
	

	whichUpgrade(pageSource)

def getPageData():
	url = "http://orteil.dashnet.org/cookieclicker/"
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read()) #Object holding source code of cookie clicker
	return soup

def calcReturn(upgradeId, pageSource):
	nextUpgrade = upgradeId++
	productId = "product" + str(upgradeId)
	nextProductId = "product" + str(nextUpgrade)
	upgradeDiv = pageSource.find("div", id=productId)
	
	
