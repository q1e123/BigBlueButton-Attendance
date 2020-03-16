from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

class DriverFirefox:
	def __init__(self,headless = False):
		self.headless = headless
		options = Options()
		profile = webdriver.FirefoxProfile()
		options.headless = headless
		self.driver = webdriver.Firefox(options=options, firefox_profile=profile)

	def goto(self,site):
		self.driver.get(site)

	def click(self,xpath):
		elem = self._find(xpath)
		elem.click()

	def send_keys(self, xpath, keys):
		elem = self._find(xpath)
		elem.send_keys(keys)

	def get_value(self,xpath,attribute):
		elem = self._find(xpath)
		return elem.get_attribute(attribute)

	def is_selected(self, xpath):
		elem = self._find(xpath)
		return elem.is_selected()

	def refresh(self):
		self.driver.refresh()

	def _find(self, xpath):
		return self.driver.find_element_by_xpath(xpath)
