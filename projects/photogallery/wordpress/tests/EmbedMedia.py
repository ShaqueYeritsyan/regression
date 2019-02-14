#~#~~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#
# Author: Shaqe Yeritsyan                                                                                      #
# Functional test cases for Photo Gallery WordPress plugin                                                     # 
# Tested options of Add Galleries/Images -> Embed Media section of the plugin                                  #
# Test Coverage: YouTube                                                                                       #
#~#~~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#

from com.lib.Browser import Browser
from com.pages.Setup import Setup
from com.pages.PhotoGalleryBack import PhotoGalleryBack

class TestEmbedMedia():
	setup = Setup()
	pgBack = PhotoGalleryBack()

	def test_setup(self):
		self.setup.setUpClass()

	def test_embed_youtube_media(self):
		self.pgBack.addGallery()
		self.pgBack.setGalleryTitle("Embed Media")
		self.pgBack.embedMedia("https://www.youtube.com/watch?v=mmCnQDUSO4I", "mmCnQDUSO4I")

	def test_embed_short_url_youtube_media(self):
		self.pgBack.embedMedia("https://youtu.be/QxHkLdQy5f0", "QxHkLdQy5f0")

	def test_embed_embedded_youtube_media_not_supported(self):
		self.pgBack.embedMedia("https://www.youtube.com/embed/mmCnQDUSO4I")
		self.pgBack.acceptAlert("The entered URL is incorrect. Please check the URL and try again.")
		self.pgBack.embedMedia("https://www.youtube.com/v/mmCnQDUSO4I")
		self.pgBack.acceptAlert("The entered URL is incorrect. Please check the URL and try again.")

		self.pgBack.publishGallery()
		self.pgBack.successfullySaving()

	def test_teardown(self):
		self.setup.tearDownClass()