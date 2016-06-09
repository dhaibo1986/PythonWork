#coding:utf8
'''
Created on 2016年5月22日

@author: Administrator
'''
import unittest
from selenium  import webdriver
from conf import bankconf
from conf.bankconf import domain,username,password
from public import login_bank
import time
import traceback

base_url = bankconf.bank_url(domain)


class test_my_account(unittest.TestCase):
    u"""我的账户各页面关键元素检查"""  
    remoteip='http://172.17.2.136:3344/wd/hub'
    @classmethod
    def setUpClass(self):
        #self.driver = webdriver.Firefox()
        self.driver=webdriver.Remote("%s"%self.remoteip,webdriver.DesiredCapabilities.FIREFOX)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        #login_bank.login_bank(self)
        login_bank.login_bank(self,username,password,domain)
        time.sleep(2)  

    def setUp(self):
        self.base_url = base_url
        self.verificationErrors = []
        self.accept_next_aler = True

        
    def test_my_safe(self):
        u"""判断安全管理页是否正确"""
        try:
            driver =  self.driver 
            driver.get(self.base_url + "/my/safe")
            time.sleep(3) 
            gettitle = driver.find_element_by_xpath("html/body/section/div[2]/div[2]/div/div[1]")
            self.assertEqual(u"个人安全信息", gettitle.text, u"个人安全信息页面异常") 
            #username_input =user_info.get("username")
            #self.assertEqual(username_input, getuname, u"个人安全信息页面异常")  

            authstate = driver.find_element_by_css_selector(".list_r.orange").text
            self.assertEqual(u"已验证", authstate, u"实名认证状态异常")             
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


    @classmethod
    def tearDownClass(self):
        self.driver.quit()  

if __name__=='__main__':
    unittest.main()       


