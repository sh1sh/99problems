# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class OlxMainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome("/Users/adam/Downloads/chromedriver")

    def setUp(self):
        self.EXPECTED_MAIN_TITLE = u'Ogłoszenia - Sprzedam, kupię na OLX.pl'

    def test_main_page(self):
        driver = self.driver
        driver.get('http://olx.pl')
        elem = driver.find_element_by_xpath('//*[@id="headerSearch"]')
        elem.send_keys("buty")
        elem.send_keys(Keys.RETURN)
        title = driver.title
        print(title)
        assert title == u'Buty - OLX.pl'

    def test_oferty_page(self):
        driver = self.driver
        driver.get('http://olx.pl/oferty/')
        elem = driver.find_element_by_id("headerLogo")
        elem.click()
        title = driver.title
        print(title)
        assert title == self.EXPECTED_MAIN_TITLE

    def test_zasady_page(self):
        driver = self.driver
        driver.get('http://olx.pl/zasady/')
        elem = driver.find_elements_by_link_text(u'Ogłoszenia')
        for i in elem:
            i.click()
        title = driver.title
        print(title)
        assert title == u'Regulamin OLX.pl'

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        #pass


if __name__ == '__main__':
    unittest.main()
