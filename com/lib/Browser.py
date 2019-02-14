from Config import Config

class Browser:

	def getDriver(self):
		self.driver = Config.environment
		return self.driver