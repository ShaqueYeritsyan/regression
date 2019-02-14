from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
import os

class Config:
	#### BROWSERS ####
	#Select the browser that you want to use for the test execution
	environment = webdriver.Firefox()
	#environment = webdriver.Chrome()

	#### URL ####
	WPBaseUrl = "https://backupqa314.000webhostapp.com/"
	WPUrl = ""

	#### User Credentials ####
	userName = "admin"
	password = "admin"

	#### PLUGIN INFO####
	project = "projects/photogallery/wordpress/"

	# In the result path you can find the results of executed scripts.
	resultPath = "results/"

	# This variable is used for waiting some processes
	time = 30