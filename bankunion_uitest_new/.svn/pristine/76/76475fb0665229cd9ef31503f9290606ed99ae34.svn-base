#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
import unittest, re ,sys
sys.path.append("..")
from conf.bankconf import bank_url,domain
#from unittest import TestLoader


base_url=bank_url(domain)

class Test_loan(unittest.TestCase):
    remoteip='http://172.17.2.136:3344/wd/hub'
    def setUp(self):
        self.driver=webdriver.Remote("%s"%self.remoteip,webdriver.DesiredCapabilities.FIREFOX)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.base_url = base_url
        self.verificationErrors = []
        self.accept_next_aler = True

    def test1(self):
        u"""合同名称验证"""
        driver=self.driver
        driver.get(self.base_url+'/help/agreement/loan')
        platform=driver.find_element_by_xpath("/html/body/div/p[3]").text
        platformname=re.search('\".*\"',platform).group().strip('\"')
        url=self.base_url.replace("http://","").replace("https://","")
        self.assertEqual(platformname, url, u"合同url错误") 
    
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
               
if __name__=="__main__":
    pass
    #===========================================================================
    # a=TestLoader()
    # print a.loadTestsFromName('test_chongzhi')
    #===========================================================================
        
