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
    def setUp(self):
#         unittest.TestCase.setUp(self)
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        login_bank.login_bank(self)
        time.sleep(2)
        self.base_url = base_url    # 将浏览器的调用和URL的访问放到初始化部分
        self.verificationErrors = []   #脚本运行时，错误的信息将被打印到这个列表中
        self.accept_next_aler = True   #是否继续接受下一下警告
        
        
       
    def test_my_safe(self):
        u"""判断安全管理页是否正确"""
        driver =  self.driver  
        getuname = driver.find_element_by_css_selector(".jl17.mess.realName").text
        username_input =user_info.get("username")
        self.assertEqual(username_input, getuname, u"个人安全信息页面异常")  
        
        authstate = driver.find_element_by_css_selector(".list_r.orange").text
        self.assertEqual(u"已验证", authstate, u"实名认证状态异常")          
        #         driver.get(self.base_url + "/my")     
     
    def test_my(self):
        u"""判断账户总览页是否正确"""
        try:
            driver =  self.driver  
            driver.get(self.base_url + "/my")
            element = driver.find_element_by_css_selector(".allCount.fl>h3")
            self.assertEqual(u"总资产", element.text, u"总资产页面异常")            
        except Exception:
            self.verificationErrors.append(str(traceback.format_exc()))    
    
        
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
       
             
if __name__=='__main__':
    unittest.main()       
        
        
        