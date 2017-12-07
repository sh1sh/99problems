# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class StrmMainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome("/Users/adam/Downloads/chromedriver")

    def setUp(self):
        self.EXPECTED_MAIN_TITLE = u'Ogłoszenia - Sprzedam, kupię na OLX.pl'

    def test_main_page(self):
        driver = self.driver
        driver.get('http://strm.pl')
        elem = driver.find_element_by_link_text('rejestracja')
        elem.click()
        user = driver.find_element_by_name('username')
        user.send_keys('klocuch13')
        passwrd = driver.find_element_by_name('password')
        passwrd.send_keys('!Password1234')
        email = driver.find_element_by_name('email')
        email.send_keys('jankowalski@gmail.com')
        regi = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div[4]/div/button')
        regi.click()
        title = driver.title
        assert title == 'Strimoid'


    @classmethod
    def tearDownClass(self):
        #self.driver.close()
        pass


if __name__ == '__main__':
    unittest.main()
