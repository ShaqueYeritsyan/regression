from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from com.lib.Browser import Browser
from com.lib.Url import Url
from Config import Config
import pytest, os
import allure

class PhotoGalleryBack:
	driver = Browser().getDriver()

	@allure.step("Click Add New gallery button")
	def addGallery(self):
		self.driver.get(Url.WPBaseUrl + Url.WPUrl + "wp-admin/admin.php?page=galleries_bwg")
		addNewButton = WebDriverWait(self.driver, Config.time).until(
			EC.visibility_of_element_located((
				By.XPATH, "//a[@class='page-title-action']")))
		addNewButton.click()

	@allure.step("Set gallery title")
	def setGalleryTitle(self, galleryTitle):
		title = WebDriverWait(self.driver, Config.time).until(
			EC.visibility_of_element_located((
				By.ID, "name")))
		title.clear()
		title.send_keys(galleryTitle)

	@allure.step("Embed Media")
	def embedMedia(self, embededMedia, mediaTitle = ""):
		embedMediaButton = WebDriverWait(self.driver, Config.time).until(
			EC.visibility_of_element_located((
				By.XPATH, "//input[@id='show_add_embed'][@value='Embed Media']")))
		embedMediaButton.click()
		embedMediaInput = WebDriverWait(self.driver, Config.time).until(
			EC.visibility_of_element_located((
				By.XPATH, "//input[@id='embed_url'][@placeholder='Enter YouTube, Vimeo, Instagram, Facebook, Flickr or Dailymotion URL here.']")))
		embedMediaInput.click()
		embedMediaInput.clear()
		embedMediaInput.send_keys(embededMedia)
		addToGalleryButton = WebDriverWait(self.driver, Config.time).until(
			EC.visibility_of_element_located((
				By.XPATH, "//input[@value='Add to gallery']")))
		addToGalleryButton.click()
		if "" != mediaTitle:
			WebDriverWait(self.driver, Config.time).until(
				EC.visibility_of_element_located((
					By.XPATH, "//td[@data-colname='Filename']//img[@title='" + mediaTitle + "']")))

	@allure.step("Publish gallery")
	def publishGallery(self):
		publishButton = WebDriverWait(self.driver, Config.time).until(
			EC.visibility_of_element_located((
				By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Gallery title'])[1]/following::button[1]")))
		publishButton.click()

	@allure.step("Validate successfully saving")
	def successfullySaving(self):
		successmessage = WebDriverWait(self.driver, Config.time).until(
			EC.visibility_of_element_located((
				By.XPATH, "//strong[.='Item successfully saved.']")))
		
	@allure.step("Check alert text and accept it")
	def acceptAlert(self, alertMessage = ""):
		WebDriverWait(self.driver, Config.time).until(
			EC.alert_is_present())
		alert = self.driver.switch_to.alert
		assert alert.text == alertMessage
		alert.accept()