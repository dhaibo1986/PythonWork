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
    u'''马上登录页各请求非200'''   
    
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        login_bank.login_bank(self)
        time.sleep(2)  
     
    def setUp(self):
        self.verificationErrors = []   #脚本运行时，错误的信息将被打印到这个列表中
        self.accept_next_aler = True   #是否继续接受下一下警告
        cookie = self.driver.get_cookies()
        print cookie 
        dict = {}
        for dic in cookie:
            dict[dic['name']]=dic['value']
        print dict
        self.headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Accept-Encoding': 'gzip, deflate',
                        'Referer': 'http://rej.jzbank.com/my'
                        }
        s = requests.Session()
        self.cookies = requests.utils.cookiejar_from_dict(dict, cookiejar=None, overwrite=True)
        resp = s.get("http://rej.jzbank.com/my",headers = self.headers,cookies=self.cookies)
        resp.text
        print resp.cookies
        self.my = MyParser.MyParser() 
        self.my.feed(resp.text)
                

 
#     def test_all_href(self): 
#         u'''我的账户 all_href'''   
#         print self.my.links
#         for url in self.my.links:
#             s = requests.Session()
#             resp  = s.get(url,cookies=self.cookies)
#             print self.cookies
#             self.assertEqual(resp.status_code,200,u"ERROR url is [" + url + u"]返回值["+str(resp.status_code)+"]")
#             print(resp.status_code,url)


    def test_all_href(self): 
        u'''我的账户 all_href'''   
        print self.my.links
        for url in self.my.links:
            try:
                if  url.find('/my/syslogout'):
                    continue
                else:
                    s = requests.Session()
                    print 'self cookies is:',self.cookies
                    resp  = s.get(url,headers=self.headers,cookies=self.cookies)
                    print 'resp cookies is:', resp.cookies
                    #print self.cookies
                    print(resp.status_code,url)
                    self.assertEqual(resp.status_code,200,u"ERROR url is [" + url + u"]返回值["+str(resp.status_code)+"]")
            except Exception:
                self.verificationErrors.append(str(traceback.format_exc()))
                traceback.format_exc()             
     
#     def test_all_css(self):
#         u'''马上登录页 all_css'''
#         print '-' * 10
#         print self.my.css
#         for url in self.my.css:
#             resp  = requests.get(url) 
#             self.assertEqual(resp.status_code, 200, u'url:'+ url + u'返回值非200')   
#             print(resp.status_code,url)        
#             
#     def test_all_img(self):
#         u'''马上登录页 all_img'''
#         print '&&&&&&&&' * 10
#         print self.my.img   
#         for url in self.my.img: 
#             resp = requests.get(url) 
#             self.assertEqual(resp.status_code, 200, u'url:'+ url + u'返回值非200') 
#             print(resp.status_code,url)  
#     
#     def test_all_js(self):
#         u'''马上登录页 all_js'''
#         print '@@@@@' * 10
#         print self.my.js
#         for url in self.my.js:
#             resp = requests.get(url)
#             self.assertEqual(resp.status_code, 200, u'url:'+ url + u'返回值非200')
#             print(resp.status_code,url) 
#                       
    

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
