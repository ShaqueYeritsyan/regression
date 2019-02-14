from com.pages.WPLogin import WPLogin
from com.lib.Browser import Browser
from com.lib.Url import Url

class Setup:
	@classmethod
	def setUpClass(inst):
		inst.browser = Browser()
		inst.driver = inst.browser.getDriver()
		inst.driver.get(Url.WPBaseUrl + Url.WPUrl + Url.WPLoginUrl)
		loginPage = WPLogin(inst.driver)
		loginPage.loginWordpress()

	@classmethod
	def tearDownClass(inst):
		inst.driver.quit()