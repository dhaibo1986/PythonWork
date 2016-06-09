#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
import unittest, time ,sys
sys.path.append("..")
from public import login_bank
from conf.bankconf import username,password,domain,bank_url

base_url=bank_url(domain)

class Tixian(unittest.TestCase):
    remoteip='http://172.17.2.136:3344/wd/hub'
    def setUp(self):
        self.driver=webdriver.Remote("%s"%self.remoteip,webdriver.DesiredCapabilities.FIREFOX)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.base_url = base_url
        self.verificationErrors = []
        self.accept_next_aler = True
    
    def test_tixian(self):
        u"""提现成功 """
        driver=self.driver
        login_bank.login_bank(self,username,password,domain)
        time.sleep(4)
        #点击我要提现
        driver.find_element_by_css_selector("section.safe div.bd div.leftMenu ul li a[href='/my/cash']").click()
        #录入提现金额
        driver.find_element_by_css_selector(" div.c-area form.cashBoxForm ul li.cf input#moneyTix.fl").send_keys('100')
        #录入交易密码
        driver.find_element_by_css_selector(' div.recharge div.c-area form.cashBoxForm ul li.cf input.fl[name="tradePwd"]').send_keys(password)
        #点击提现
        driver.find_element_by_css_selector("div.recharge div.c-area form.cashBoxForm ul li.sub input.normalBtn").click()
        time.sleep(2)
        #点击确定
        driver.find_element_by_css_selector(" div.aui_buttons button.aui_state_highlight").click()
        time.sleep(2)
        #提现申请已经提交
        tixian_text=driver.find_element_by_css_selector(" div.aui_inner table.aui_dialog tbody tr td.aui_main div.aui_content").text
        self.assertEqual(tixian_text, u'提现申请已提交！', u'提现失败')


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__=="__main__":
    unittest.main()    
        
