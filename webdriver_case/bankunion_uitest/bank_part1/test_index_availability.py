#encoding=utf-8
'''
Created on 2016年5月21日

@author: Administrator
'''

import unittest
import requests
# from conf import bankconf
from bank_part1 import MyParser
     

class Index_avaliability_Test(unittest.TestCase):
    u'''测试首页各请求非200'''    
    def setUp(self):
        #base_url=bankconf.bank_url()
        #resp = requests.get(base_url)
        resp = requests.get("http://e.jzctb.com")
        
        self.my = MyParser.MyParser() 
        self.my.feed(resp.text)
        
        
    def test_all_href(self): 
        u'''测试首页 all_href'''
        print '%%%%%%' * 10     
        print self.my.links
        for url in self.my.links:
            resp  = requests.get(url)
            self.assertEqual(resp.status_code,200,u"ERROR url is [" + url + u"]返回值["+str(resp.status_code)+u"]非200")
            print(resp.status_code,url)
    
 
    def test_all_css(self):
        u'''测试首页 all_css'''
        print '-' * 10
        print self.my.css
        for url in self.my.css:
            resp  = requests.get(url) 
            self.assertEqual(resp.status_code, 200, u'url:'+ url + u'返回值非200')   
            print(resp.status_code,url)        
            
    def test_all_img(self):
        u'''测试首页 all_img'''
        print '&&&&&&&&' * 10
        print self.my.img   
        for url in self.my.img: 
            resp = requests.get(url) 
            self.assertEqual(resp.status_code, 200, u'url:'+ url + u'返回值非200') 
            print(resp.status_code,url)  
    
    def test_all_js(self):
        u'''测试首页 all_js'''
        print '@@@@@' * 10
        print self.my.js
        for url in self.my.js:
            resp = requests.get(url)
            self.assertEqual(resp.status_code, 200, u'url:'+ url + u'返回值非200')
            print(resp.status_code,url) 
                      
    
    def tearDown(self):
        if self.my:
            self.my.close()


    
if __name__=='__main__':
    unittest.main()   



