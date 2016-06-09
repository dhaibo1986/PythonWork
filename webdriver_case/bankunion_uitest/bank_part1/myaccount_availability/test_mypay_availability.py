#encoding=utf-8
'''
Created on 2016年5月21日

@author: Administrator
'''

import unittest
import requests
from bank_part1 import MyParser
from bank_websitecase.public import login_bank
from selenium  import webdriver
from conf import bankconf 
import time
import traceback

base_url = bankconf.bank_url()
username_input,password =bankconf.userinfo()

class test_passport_availability(unittest.TestCase):
    u'''我要充值各请求非200'''   

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        #self.driver.implicitly_wait(5)
        login_bank.login_bank(self)
        time.sleep(5)  

    def setUp(self):
        self.verificationErrors = []
        self.accept_next_aler = True 
        cookie = self.driver.get_cookies()
        #print cookie 
        dict = {}
        for dic in cookie:
            dict[dic['name']]=dic['value']
        print dict
        s = requests.Session()
        self.cookies = requests.utils.cookiejar_from_dict(dict, cookiejar=None, overwrite=True)
        resp = s.get("http://rej.jzbank.com/my/pay",cookies=self.cookies)
        resp.text
        #print resp.cookies
        self.mypay = MyParser.MyParser() 
        self.mypay.feed(resp.text)
        print 'setUp'

    def test_all_href(self): 
        u'''我要充值 all_href'''   
        #print self.mypay.links
        for url in self.mypay.links:
            try:
                s = requests.Session()
                #print 'self cookies is:',self.cookies
                resp  = s.get(url,cookies=self.cookies)
                #print 'resp cookies is:', resp.cookies
                print(resp.status_code,url)
                self.assertEqual(resp.status_code,200,u"ERROR url is [" + url + u"]返回值["+str(resp.status_code)+"]")
            except Exception:
                self.verificationErrors.append(str(traceback.format_exc()))
                traceback.format_exc()             
 
    def test_all_css(self):
        u'''我要充值 all_css'''
        #print self.mypay.css
        for url in self.mypay.css:
            try:
                s = requests.Session()
                resp  = s.get(url,cookies=self.cookies) 
                print(resp.status_code,url)        
                self.assertEqual(resp.status_code, 200, u"ERROR url is [" + url + u"]返回值["+str(resp.status_code)+"]") 
            except Exception:
                self.verificationErrors.append(str(traceback.format_exc()))
                traceback.format_exc()     

    def test_all_img(self):
        u'''我要充值 all_img'''
        print self.mypay.img
        for url in self.mypay.img:
            try:
                s = requests.Session()
                resp  = s.get(url,cookies=self.cookies) 
                print(resp.status_code,url)        
                self.assertEqual(resp.status_code, 200, u"ERROR url is [" + url + u"]返回值["+str(resp.status_code)+"]") 
            except Exception:
                self.verificationErrors.append(str(traceback.format_exc()))
                traceback.format_exc()  
                            
    def test_all_js(self):
        u'''我要充值 all_js'''
        #print self.mypay.js
        for url in self.mypay.js:
            try:
                s = requests.Session()
                resp  = s.get(url,cookies=self.cookies) 
                print(resp.status_code,url)        
                self.assertEqual(resp.status_code, 200, u"ERROR url is [" + url + u"]返回值["+str(resp.status_code)+"]") 
            except Exception:
                self.verificationErrors.append(str(traceback.format_exc()))
                traceback.format_exc()  

    def tearDown(self):
        if self.mypay:
            self.mypay.close()
        self.assertEqual([], self.verificationErrors)
        print 'tearDown'

    @classmethod
    def tearDownClass(self):
        self.driver.quit()  
        print 'end'

if __name__=='__main__':
    unittest.main()   
