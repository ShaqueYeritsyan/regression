from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Config import Config
import pytest
import allure

class WPLogin:
	def __init__(self, driver):
		self.driver = driver

		self.email_field = WebDriverWait(self.driver, Config.time).until(
			EC.element_to_be_clickable((
				By.XPATH, "//input[@id='user_login']")))

		self.password_field = WebDriverWait(self.driver, Config.time).until(
			EC.visibility_of_element_located((
				By.XPATH, "//input[@id='user_pass']")))

		self.login_button = WebDriverWait(self.driver, Config.time).until(
			EC.visibility_of_element_located((
				By.XPATH, "//input[@id='wp-submit']")))

	@allure.step("Login WordPress")
	def loginWordpress(self):
		self.email_field.click()
		self.email_field.clear()
		self.email_field.send_keys(Config.userName)
		self.password_field.click()
		self.password_field.clear()
		self.password_field.send_keys(Config.password)
		self.login_button.click()
		WebDriverWait(self.driver, Config.time).until(EC.presence_of_element_located((By.ID, "footer-thankyou")))