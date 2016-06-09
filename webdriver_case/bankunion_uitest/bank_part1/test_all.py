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
from time import sleep

base_url = bankconf.bank_url()
username_input,password =bankconf.userinfo()

class test_all(unittest.TestCase):
    u'''我的账户页各请求非200'''   
    BASE_URL = base_url

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        
        login_bank.login_bank(self)
        time.sleep(2)  

    def setUp(self):
        self.verificationErrors = []
        self.accept_next_aler = True 
        cookie = self.driver.get_cookies()
        #print cookie 
        dict = {}
        for dic in cookie:
            dict[dic['name']]=dic['value']
        print dict
        self.headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Accept-Encoding': 'gzip, deflate',
                        'Referer': self.BASE_URL
                        }
        s = requests.Session()
        self.cookies = requests.utils.cookiejar_from_dict(dict, cookiejar=None, overwrite=True)
        dict = {'index':'/',
                'bidlist':'/bid/list/',
                'my':'/my',                
                'myinvestment':'/my/investment',
                'mypay':'/my/pay',
                'mycash':'/my/cash',
                'mysafe/':'/my/safe/',
                'mymessage':'/my/message',
                'help':'/help/guide'
                }
        if self.BASE_URL != None or self.BASE_URL != '':
            self.my = MyParser.MyParser() 
            for key,value in dict.items():
                resp = s.get(self.BASE_URL + value,headers = self.headers,cookies=self.cookies)
                self.my.feed(resp.text)
    
    def test_all_href(self): 
        u'''我的账户 all_href'''   
        print self.my.links
        for url in self.my.links:
            try:
                s = requests.Session()
                #print 'self cookies is:',self.cookies
                resp  = s.get(url,headers=self.headers,cookies=self.cookies)
                #print 'resp cookies is:', resp.cookies
                print(resp.status_code,url)
                self.assertEqual(resp.status_code,200,u"ERROR url is [" + url + u"]返回值["+str(resp.status_code)+"]")
                sleep(0.1)
            except Exception:
                self.verificationErrors.append(str(traceback.format_exc()))
                traceback.format_exc()             

    def test_all_css(self): 
        u'''我的账户 all_css'''   
        print self.my.css
        for url in self.my.css:
            try:
                s = requests.Session()
                resp  = s.get(url,headers=self.headers,cookies=self.cookies)
                print(resp.status_code,url)
                self.assertEqual(resp.status_code,200,u"ERROR url is [" + url + u"]返回值["+str(resp.status_code)+"]")
            except Exception:
                self.verificationErrors.append(str(traceback.format_exc()))
                traceback.format_exc()

    def test_all_img(self): 
        u'''我的账户 all_img'''   
        print self.my.img
        for url in self.my.img:
            try:
                s = requests.Session()
                resp  = s.get(url,headers=self.headers,cookies=self.cookies)
                print(resp.status_code,url)
                self.assertEqual(resp.status_code,200,u"ERROR url is [" + url + u"]返回值["+str(resp.status_code)+"]")
            except Exception:
                self.verificationErrors.append(str(traceback.format_exc()))
                traceback.format_exc()
                
    def test_all_js(self): 
        u'''我的账户 all_js'''   
        print self.my.js
        for url in self.my.js:
            try:
                s = requests.Session()
                resp  = s.get(url,headers=self.headers,cookies=self.cookies)
                print(resp.status_code,url)
                self.assertEqual(resp.status_code,200,u"ERROR url is [" + url + u"]返回值["+str(resp.status_code)+"]")
            except Exception:
                self.verificationErrors.append(str(traceback.format_exc()))
                traceback.format_exc()

    def tearDown(self):
        if self.my:
            self.my.close()
        self.assertEqual([], self.verificationErrors)
        print 'tearDown'

    @classmethod
    def tearDownClass(self):
        self.driver.quit()  

if __name__=='__main__':
    unittest.main()   
