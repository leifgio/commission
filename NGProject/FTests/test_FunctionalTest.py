from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys 
import time
from django.test import LiveServerTestCase




class PageTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def test_start_list_and_retrieve_it(self):
		self.browser.get(self.live_server_url)
		self.assertIn('NutriGeek', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('NutriGeek', headerText)

		inpNewFName = self.browser.find_element_by_id('fname')
		inpNewFName.send_keys('Kath Labad Labad')
		time.sleep(1)

		gender = self.browser.find_element_by_id('gender1')
		gender.click()

		inpNewAge= self.browser.find_element_by_id('age1')
		inpNewAge.send_keys('21')
		time.sleep(1)

		inpNewEAdd= self.browser.find_element_by_id('EAdd')
		inpNewEAdd.send_keys('kathleenmae.labadlabad@gsfe.tupcavite.edu.ph')
		time.sleep(1)

		inpNewEHeight= self.browser.find_element_by_id('EHeight')
		inpNewEHeight.send_keys('150')
		time.sleep(1)

		inpNewEWeight= self.browser.find_element_by_id('EWeight')
		inpNewEWeight.send_keys('45')
		time.sleep(1)

		Allergen6 = self.browser.find_element_by_id('Allergen6')
		Allergen6.click()


		btnkath = self.browser.find_element_by_id('btnkath')
		self.assertEqual (inpNewFName.get_attribute('placeholder'), 'Enter your full name here.')

		btnkath.click()
		time.sleep(1)

		inpNewFName = self.browser.find_element_by_id('fname')
		inpNewFName.send_keys('Jamal Berande')
		time.sleep(1)

		gender = self.browser.find_element_by_id('gender')
		gender.click()

		inpNewAge= self.browser.find_element_by_id('age1')
		inpNewAge.send_keys('22')
		time.sleep(1)

		inpNewEAdd= self.browser.find_element_by_id('EAdd')
		inpNewEAdd.send_keys('jamal.berande@tup.edu.ph')
		time.sleep(1)

		inpNewEHeight= self.browser.find_element_by_id('EHeight')
		inpNewEHeight.send_keys('165')
		time.sleep(1)

		inpNewEWeight= self.browser.find_element_by_id('EWeight')
		inpNewEWeight.send_keys('55')
		time.sleep(1)

		Allergen6 = self.browser.find_element_by_id('Allergen4')
		Allergen6.click()

		

		btnkath = self.browser.find_element_by_id('btnkath')
		self.assertEqual (inpNewFName.get_attribute('placeholder'), 'Enter your full name here.')

		btnkath.click()
		time.sleep(1)


	def checking_if_in_table_list(self,row_test):
		table = self.browser.find_element_by_tag_name('table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Kath Labad Labad', 'Female', '21', 'kathleenmae.labadlabad@gsfe.tupcavite.edu.ph','150', '45', 'Tree nuts', [rows.text for rows in rows])


#if __name__=='__main__':
#	unittest.main(warnings='ignore')

