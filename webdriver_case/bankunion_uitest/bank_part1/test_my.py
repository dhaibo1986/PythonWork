#coding:utf8
'''
Created on 2016年5月22日

@author: Administrator
'''
import unittest
from selenium  import webdriver
from conf import bankconf
from bank_websitecase.public import login_bank
import time
from conf.bankconf import user_info
from selenium.common.exceptions import NoSuchElementException
import traceback

base_url = bankconf.bank_url()
username_input,password =bankconf.userinfo()

class my_account(unittest.TestCase):
    u"""测试我的账户"""  
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        login_bank.login_bank(self)
        time.sleep(2)  
#         unittest.TestCase.setUp(self)
        
    def setUp(self):
        self.base_url = base_url    # 将浏览器的调用和URL的访问放到初始化部分
        self.verificationErrors = []   #脚本运行时，错误的信息将被打印到这个列表中
        self.accept_next_aler = True   #是否继续接受下一下警告
        print 'setUp'
        
        
       
    def test_my_safe(self):
        u"""判断安全管理页是否正确"""
        try:
            driver =  self.driver  
            getuname = driver.find_element_by_xpath(".//*[@id='content_auth']/li[1]/span[4]").text   #??
            username_input =user_info.get("username")
            self.assertEqual(username_input, getuname, u"个人安全信息页面异常")  
             
            authstate = driver.find_element_by_css_selector(".list_r.orange").text
            self.assertEqual(u"已验证", authstate, u"实名认证状态异常")          
            #         driver.get(self.base_url + "/my")     
        except Exception:
            self.verificationErrors.append(str(traceback.format_exc()))    
             
    def test_my(self):
        u"""判断账户总览页是否正确"""
        try:
            driver =  self.driver  
            driver.get(self.base_url + "/my")
            time.sleep(3)
            element = driver.find_element_by_css_selector(".allCount.fl>h3")
            self.assertEqual(u"总资产", element.text, u"总资产页面异常")   
#             driver.find_element_by_xpath("html/body/section/div[2]/div[2]/div[2]/div[2]/ul/li[1]/a").click()
#             element = driver.find_element_by_xpath("html/body/section/div[2]/div[2]/div[1]/h3")
#             self.assertEqual(u"收支明细", element.text, u"收支明细页面异常")         
        except Exception:
            self.verificationErrors.append(str(traceback.format_exc()))    
     
    def test_my_investment(self):
        u"""判断投资管理页是否正确"""
        try:
            driver =  self.driver  
            driver.get(self.base_url + "/my/investment")
            time.sleep(3)
            element = driver.find_element_by_css_selector(".h-title.posr>h3")
            self.assertEqual(u"投资管理", element.text, u"投资管理产页面异常")   
         
        except Exception:
            self.verificationErrors.append(str(traceback.format_exc()))    
     
    def test_my_pay(self):
        u"""判断我要充值页是否正确"""
        try:
            driver =  self.driver  
            driver.get(self.base_url + "/my/pay")
            time.sleep(3)
            element = driver.find_element_by_id("chongzhi")
            self.assertIsNotNone(element, u"我要充值页面异常")             
        except Exception:
            self.verificationErrors.append(str(traceback.format_exc()))     
    
    def test_my_cash(self):
        u"""判断我要提现页是否正确"""
        try:
            driver =  self.driver  
            driver.get(self.base_url + "/my/cash")
            time.sleep(3)
            element = driver.find_element_by_xpath("//input[@type='submit' and @value='提现']")
            self.assertIsNotNone(element, u"我要提现页面异常")          
        except Exception:
            self.verificationErrors.append(str(traceback.format_exc()))    
                             
        
    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
        print 'tearDown'
        
    @classmethod
    def tearDownClass(self):
        self.driver.quit()  
             
if __name__=='__main__':
    unittest.main()       
        
        
        