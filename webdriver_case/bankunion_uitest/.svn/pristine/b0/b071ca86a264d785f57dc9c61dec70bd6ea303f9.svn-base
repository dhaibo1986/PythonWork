#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
import unittest, time ,sys
sys.path.append("..")
from public import login_bank
from conf import bankconf
from page_element import bank_page
from conf.bankconf import borrowamount
base_url=bankconf.bank_url()
username_input,password =bankconf.userinfo()

class Toubiao(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote("http://172.17.2.136:3344/wd/hub",webdriver.DesiredCapabilities.FIREFOX)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.base_url = base_url
        self.verificationErrors = []
        self.accept_next_aler = True
    
    def test_toubiao_1(self):
        u"""测试投标后金额减少"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击我要投资
        elements_home=bank_page.home_page(self)
        elements_home.get("woyaotouzi").click()
        #选择第一个投标按钮进行投标
        keyongbiao=driver.find_elements_by_css_selector(" li span.c7 a.tender-btn")
        keyongbiao[0].click()
        #跳转到标详情页面
        elements=bank_page.woyaotouzi_tzlb(self)
        wodeyue=elements.get("wodeyue").get_attribute("num")
        print u"投标前余额",wodeyue
        elements.get("toubiaojine").send_keys("100")
        elements.get("lijitoubiao").click()
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight[type='button']").click()
        time.sleep(2)
        now_yue=driver.find_element_by_css_selector(" span#yi span#memberyue").get_attribute("num")
        #now_yue_e=WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector(" span#yi span#memberyue"))
        print u"投标后余额",now_yue
        toubiaojine=float(wodeyue)-float(now_yue)
        self.assertEqual(toubiaojine, 100.0, u"用户余额未减少")
            
    def test_toubiao_2(self):
        u"""测试投标后投标人次增加"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击我要投资
        elements_home=bank_page.home_page(self)
        elements_home.get("woyaotouzi").click()
        #选择第一个投标按钮进行投标
        keyongbiao=driver.find_elements_by_css_selector(" li span.c7 a.tender-btn")
        keyongbiao[0].click()
        #跳转到标详情页面
        elements=bank_page.woyaotouzi_tzlb(self)
        #投标前投标人数
        toubiao_num_before=int(driver.find_element_by_css_selector("h3.bright span#count").text)
        elements.get("toubiaojine").send_keys("100")
        elements.get("lijitoubiao").click()
        driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight[type='button']").click()
        time.sleep(2)
        #投标后人投标人数
        toubiao_num_after=int(driver.find_element_by_css_selector("h3.bright span#count").text)
        self.assertEqual(toubiao_num_before+1,toubiao_num_after,u"投标记录未增加")

    def test_toubiaochaoe(self):
        u"""测试超额投标"""
        driver=self.driver
        login_bank.login_bank(self)
        #点击我要投资
        elements_home=bank_page.home_page(self)
        elements_home.get("woyaotouzi").click()
        #选择第指定标进行投标
        n = 0
        bidname_list=driver.find_elements_by_css_selector("div.p-list ul#indexList li span.c2 a")
        for bidname in bidname_list:
            n+=1
            if u"按月付息第1期" in bidname.text:
                break

        keyongbiao_list=driver.find_elements_by_css_selector(" li span.c7 a.tender-btn")
        keyongbiao_list[n-1].click()
        #跳转到标详情页面
        elements=bank_page.woyaotouzi_tzlb(self)
        #已超额，请重新输入！
        jine=int(borrowamount)*10000+100
        elements.get("toubiaojine").send_keys("%s"%jine)
        elements.get("lijitoubiao").click()
        time.sleep(2)
        chaoetishi = driver.find_element_by_css_selector("table.aui_dialog tbody tr td.aui_main div.aui_content").text
        self.assertEqual(u"已超额，请重新输入！", chaoetishi, u"超额投标失败")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__=='__main__':
    unittest.main()
