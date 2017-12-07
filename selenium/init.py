# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver


class OlxMainTests(unittest.TestCase):
    def test_main_page(self):
        driver = webdriver.Chrome("/Users/adam/Downloads/chromedriver")
        driver.get('http://olx.pl')
        title = driver.title
        print(title)
        assert title == u'Ogłoszenia - Sprzedam, kupię na OLX.pl'
        driver.close()

    def test_oferty_page(self):
        driver = webdriver.Chrome("/Users/adam/Downloads/chromedriver")
        driver.get('http://olx.pl/oferty/')
        title = driver.title
        print(title)
        assert title == u'Ogłoszenia - Sprzedam, kupię na OLX.pl'
        driver.close()
