#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
import unittest, time ,sys
sys.path.append("..")
from public import login_bank
from conf import bankconf

base_url=bankconf.bank_url()
username_input,password =bankconf.userinfo()

class Woyaochongzhi(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote("http://172.19.2.136:3345/wd/hub",webdriver.DesiredCapabilities.FIREFOX)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.base_url = base_url
        self.verificationErrors = []
        self.accept_next_aler = True
          
    def test_icbc(self):
        u"""跳转工商银行"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击充值按钮
        time.sleep(1)
        driver.get(self.base_url+'/my')
        driver.find_element_by_css_selector("div.bd:nth-child(2) div.payCash a[href='/my/pay'][class='payBtn fl']").click()
        driver.find_element_by_css_selector("ul.cf li label img[src$='icbc.png']").click()
        driver.find_element_by_css_selector("li input#money.active").send_keys("100")
        driver.find_element_by_css_selector("li input#chongzhi").click()
        now_window=driver.current_window_handle
        #点击弹出确定按钮
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight").click()
        time.sleep(3)
        all_windows=driver.window_handles
        current_url=''
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                driver.find_elements_by_xpath("/html/body/table")
                current_url=driver.current_url
        self.assertIn(u"b2c.icbc.com.cn",current_url,u"工商银行跳转失败")
   
    def test_cmb(self):
        u"""跳转招商银行"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击充值按钮
        time.sleep(1)
        driver.get(self.base_url+'/my')
        driver.find_element_by_css_selector("div.bd:nth-child(2) div.payCash a[href='/my/pay'][class='payBtn fl']").click()
        driver.find_element_by_css_selector("ul.cf li label img[src$='cmb.png']").click()
        driver.find_element_by_css_selector("li input#money.active").send_keys("100")
        driver.find_element_by_css_selector("li input#chongzhi").click()
        now_window=driver.current_window_handle
        #点击弹出确定按钮
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight").click()
        time.sleep(3)
        all_windows=driver.window_handles
        current_url=""
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                driver.find_element_by_css_selector(" div.divPageBg div div#AllElementContainer div")
                current_url=driver.current_url
                print current_url
        self.assertIn(u"netpay.cmbchina.com",current_url,u"招商银行跳转失败")
   
    def test_ccb(self):
        u"""跳转建设银行"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击充值按钮
        time.sleep(1)
        driver.get(self.base_url+'/my')
        driver.find_element_by_css_selector("div.bd:nth-child(2) div.payCash a[href='/my/pay'][class='payBtn fl']").click()
        driver.find_element_by_css_selector("ul.cf li label img[src$='ccb.png']").click()
        driver.find_element_by_css_selector("li input#money.active").send_keys("100")
        driver.find_element_by_css_selector("li input#chongzhi").click()
        now_window=driver.current_window_handle
        #点击弹出确定按钮
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight").click()
        time.sleep(3)
        all_windows=driver.window_handles
        current_url=''
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                driver.find_element_by_css_selector("div#PayContainer.PayForContainer_Head div.PayForContainer_Head_WebService")
                current_url=driver.current_url
                print current_url
        self.assertIn(u"ccb.com.cn",current_url,u"建设银行跳转失败")
           
    def test_abc(self):
        u"""跳转中国农业银行"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击充值按钮
        time.sleep(1)
        driver.get(self.base_url+'/my')
        driver.find_element_by_css_selector("div.bd:nth-child(2) div.payCash a[href='/my/pay'][class='payBtn fl']").click()
        driver.find_element_by_css_selector("ul.cf li label img[src$='.png']").click()
        driver.find_element_by_css_selector("li input#money.active").send_keys("100")
        driver.find_element_by_css_selector("li input#chongzhi").click()
        now_window=driver.current_window_handle
        #点击弹出确定按钮
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight").click()
        time.sleep(3)
        all_windows=driver.window_handles
        current_url=''
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                driver.find_elements_by_xpath("//table/tbody/tr/td/table/tbody/tr/td")
                current_url=driver.current_url
                print current_url
        self.assertIn(u"pay.abchina.com",current_url,u"农业银行跳转失败")    
   
    def test_boc(self):
        u"""跳转中国银行"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击充值按钮
        time.sleep(1)
        driver.get(self.base_url+'/my')
        driver.find_element_by_css_selector("div.bd:nth-child(2) div.payCash a[href='/my/pay'][class='payBtn fl']").click()
        driver.find_element_by_css_selector("ul.cf li label img[src$='boc.png']").click()
        driver.find_element_by_css_selector("li input#money.active").send_keys("100")
        driver.find_element_by_css_selector("li input#chongzhi").click()
        now_window=driver.current_window_handle
        #点击弹出确定按钮
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight").click()
        time.sleep(3)
        all_windows=driver.window_handles
        current_url=''
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                driver.find_element_by_xpath("/html/body/div[2]/div[@class='order-list']/h3")
                current_url=driver.current_url
                print current_url
        self.assertIn(u"ebspay.boc.cn",current_url,u"中国银行跳转失败")    
  
    def test_bocm(self):
        u"""跳转交通银行"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击充值按钮
        time.sleep(1)
        driver.get(self.base_url+'/my')
        driver.find_element_by_css_selector("div.bd:nth-child(2) div.payCash a[href='/my/pay'][class='payBtn fl']").click()
        driver.find_element_by_css_selector("ul.cf li label img[src$='bocm.png']").click()
        driver.find_element_by_css_selector("li input#money.active").send_keys("100")
        driver.find_element_by_css_selector("li input#chongzhi").click()
        now_window=driver.current_window_handle
        #点击弹出确定按钮
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight").click()
        time.sleep(3)
        all_windows=driver.window_handles
        current_url=''
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                driver.find_element_by_xpath("/html/body/div/div/div/div[2]")
                current_url=driver.current_url
                print current_url
        self.assertIn(u"95559.com.cn",current_url,u"交通银行跳转失败") 
  
    def test_cmbm(self):
        u"""跳转民生银行"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击充值按钮
        time.sleep(1)
        driver.get(self.base_url+'/my')
        driver.find_element_by_css_selector("div.bd:nth-child(2) div.payCash a[href='/my/pay'][class='payBtn fl']").click()
        driver.find_element_by_css_selector("ul.cf li label img[src$='cmbc.png']").click()
        driver.find_element_by_css_selector("li input#money.active").send_keys("100")
        driver.find_element_by_css_selector("li input#chongzhi").click()
        now_window=driver.current_window_handle
        #点击弹出确定按钮
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight").click()
        time.sleep(3)
        all_windows=driver.window_handles
        current_url=''
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                driver.find_element_by_xpath("/html/body/div[2]/div[7]/div/div")
                current_url=driver.current_url
                print current_url
        self.assertIn(u"cmbc.com.cn",current_url,u"民生银行跳转失败") 
  
    def test_cebb(self):
        u"""跳转光大银行"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击充值按钮
        time.sleep(1)
        driver.get(self.base_url+'/my')
        driver.find_element_by_css_selector("div.bd:nth-child(2) div.payCash a[href='/my/pay'][class='payBtn fl']").click()
        driver.find_element_by_css_selector("ul.cf li label img[src$='cebb.png']").click()
        driver.find_element_by_css_selector("li input#money.active").send_keys("100")
        driver.find_element_by_css_selector("li input#chongzhi").click()
        now_window=driver.current_window_handle
        #点击弹出确定按钮
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight").click()
        time.sleep(3)
        all_windows=driver.window_handles
        current_url=''
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                driver.find_element_by_xpath("//div/div[2]/table/tbody/tr/td/table/tbody")
                current_url=driver.current_url
                print current_url
        self.assertIn(u"cebbank.com",current_url,u"光大银行跳转失败") 
  
    def test_gdb(self):
        u"""跳转广发银行"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击充值按钮
        time.sleep(1)
        driver.get(self.base_url+'/my')
        driver.find_element_by_css_selector("div.bd:nth-child(2) div.payCash a[href='/my/pay'][class='payBtn fl']").click()
        driver.find_element_by_css_selector("ul.cf li label img[src$='gdb.png']").click()
        driver.find_element_by_css_selector("li input#money.active").send_keys("100")
        driver.find_element_by_css_selector("li input#chongzhi").click()
        now_window=driver.current_window_handle
        #点击弹出确定按钮
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight").click()
        time.sleep(3)
        all_windows=driver.window_handles
        current_url=''
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                driver.find_element_by_xpath("/html/body/div[2]/div/table/tbody/tr/td/div")
                current_url=driver.current_url
                print current_url
        self.assertIn(u"cgbchina.com.cn",current_url,u"广发银行跳转失败")
  
    def test_ecitic(self):
        u"""跳转中信银行"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击充值按钮
        time.sleep(1)
        driver.get(self.base_url+'/my')
        driver.find_element_by_css_selector("div.bd:nth-child(2) div.payCash a[href='/my/pay'][class='payBtn fl']").click()
        driver.find_element_by_css_selector("ul.cf li label img[src$='ecitic.png']").click()
        driver.find_element_by_css_selector("li input#money.active").send_keys("100")
        driver.find_element_by_css_selector("li input#chongzhi").click()
        now_window=driver.current_window_handle
        #点击弹出确定按钮
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight").click()
        time.sleep(3)
        all_windows=driver.window_handles
        current_url=''
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                driver.find_element_by_xpath("/html/body/div")
                current_url=driver.current_url
                print current_url
        self.assertIn(u"ecitic.com",current_url,u"中信银行跳转失败")
     
      
 
    def test_chainapay(self):
        u"""跳转银联充值"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击充值按钮
        time.sleep(1)
        driver.get(self.base_url+'/my')
        driver.find_element_by_css_selector("div.bd:nth-child(2) div.payCash a[href='/my/pay'][class='payBtn fl']").click()
        driver.find_element_by_css_selector("ul.cf li label img[src$='chinapay.png']").click()
        driver.find_element_by_css_selector("li input#money.active").send_keys("100")
        driver.find_element_by_css_selector("li input#chongzhi").click()
        now_window=driver.current_window_handle
        #点击弹出确定按钮
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight").click()
        time.sleep(3)
        all_windows=driver.window_handles
        current_url=''
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                driver.find_element_by_xpath("/html/body/div[3]/div/div/p")
                current_url=driver.current_url
                print current_url
        self.assertIn(u"101.231.204.87",current_url,u"银联支付跳转失败")
 
    def test_nbb(self):
        u"""跳转宁波银行"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击充值按钮
        time.sleep(1)
        driver.get(self.base_url+'/my')
        driver.find_element_by_css_selector("div.bd:nth-child(2) div.payCash a[href='/my/pay'][class='payBtn fl']").click()
        driver.find_element_by_css_selector("ul.cf li label img[src$='nbb.png']").click()
        driver.find_element_by_css_selector("li input#money.active").send_keys("100")
        driver.find_element_by_css_selector("li input#chongzhi").click()
        now_window=driver.current_window_handle
        #点击弹出确定按钮
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight").click()
        time.sleep(3)
        all_windows=driver.window_handles
        current_url=''
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody")
                current_url=driver.current_url
                print current_url
        self.assertIn(u"nbcb.com.cn",current_url,u"宁波银行跳转失败")
 
    def test_bob(self):
        u"""跳转北京银行"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击充值按钮
        time.sleep(1)
        driver.get(self.base_url+'/my')
        driver.find_element_by_css_selector("div.bd:nth-child(2) div.payCash a[href='/my/pay'][class='payBtn fl']").click()
        driver.find_element_by_css_selector("ul.cf li label img[src$='bob.png']").click()
        driver.find_element_by_css_selector("li input#money.active").send_keys("100")
        driver.find_element_by_css_selector("li input#chongzhi").click()
        now_window=driver.current_window_handle
        #点击弹出确定按钮
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight").click()
        time.sleep(3)
        all_windows=driver.window_handles
        current_url=''
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                driver.find_elements_by_xpath("/html/body/div/div[2]/div/div")
                current_url=driver.current_url
                print current_url
        self.assertIn(u"bankofbeijing.com.cn",current_url,u"北京银行跳转失败")
  

    def test_njcb(self):
        u"""跳转南京银行"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击充值按钮
        time.sleep(1)
        driver.get(self.base_url+'/my')
        driver.find_element_by_css_selector("div.bd:nth-child(2) div.payCash a[href='/my/pay'][class='payBtn fl']").click()
        driver.find_element_by_css_selector("ul.cf li label img[src$='njcb.png']").click()
        driver.find_element_by_css_selector("li input#money.active").send_keys("100")
        driver.find_element_by_css_selector("li input#chongzhi").click()
        now_window=driver.current_window_handle
        #点击弹出确定按钮
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight").click()
        time.sleep(3)
        all_windows=driver.window_handles
        current_url=''
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                driver.find_elements_by_xpath("/html/body/div[2]/div/img")
                current_url=driver.current_url
                print current_url
        self.assertIn(u"ebank.njcb.com.cn",current_url,u"南京银行跳转失败")

    def test_bos(self):
        u"""跳转上海银行"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击充值按钮
        time.sleep(1)
        driver.get(self.base_url+'/my')
        driver.find_element_by_css_selector("div.bd:nth-child(2) div.payCash a[href='/my/pay'][class='payBtn fl']").click()
        driver.find_element_by_css_selector("ul.cf li label img[src$='bos.jpg']").click()
        driver.find_element_by_css_selector("li input#money.active").send_keys("100")
        driver.find_element_by_css_selector("li input#chongzhi").click()
        now_window=driver.current_window_handle
        #点击弹出确定按钮
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight").click()
        time.sleep(3)
        all_windows=driver.window_handles
        current_url=''
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                driver.find_elements_by_xpath("/html/body/div[2]/div/div[2]")
                current_url=driver.current_url
                print current_url
        self.assertIn(u"epay.bankofshanghai.com",current_url,u"上海银行跳转失败")
 
    def test_bea(self):
        u"""跳转东亚银行"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击充值按钮
        time.sleep(1)
        driver.get(self.base_url+'/my')
        driver.find_element_by_css_selector("div.bd:nth-child(2) div.payCash a[href='/my/pay'][class='payBtn fl']").click()
        driver.find_element_by_css_selector("ul.cf li label img[src$='bea.jpg']").click()
        driver.find_element_by_css_selector("li input#money.active").send_keys("100")
        driver.find_element_by_css_selector("li input#chongzhi").click()
        now_window=driver.current_window_handle
        #点击弹出确定按钮
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight").click()
        time.sleep(3)
        all_windows=driver.window_handles
        current_url=''
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                driver.find_elements_by_xpath("/html/body/table/tbody/tr/td/div")
                current_url=driver.current_url
                print current_url
        self.assertIn(u"ebank.hkbea.com.cn",current_url,u"东亚银行跳转失败")
 


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__=='__main__':
    unittest.main()
