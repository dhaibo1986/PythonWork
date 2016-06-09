#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
import unittest, time ,sys
sys.path.append("..")
from public import login_bank
from page_element import bank_page
from conf.bankconf import username,password,domain,bank_url,return_bidconf
from conf.db_conf import Bankunion_proc
from public import yicixingjinjian
base_url=bank_url(domain)

class Toubiao(unittest.TestCase):
    remoteip='http://172.17.2.136:3344/wd/hub'
    def setUp(self):
        self.driver=webdriver.Remote("%s"%self.remoteip,webdriver.DesiredCapabilities.FIREFOX)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.base_url = base_url
        self.verificationErrors = []
        self.accept_next_aler = True
    
    def test_toubiao_1(self):
        u"""测试投标后金额减少"""
        driver=self.driver
        con=Bankunion_proc()
        def toubiao():
            con=Bankunion_proc()
            biao_id=con.back_biaoid(bankname=domain,bidstatus=16,value_way=2,product_type=1)
            login_bank.login_bank(self,username,password,domain)
            driver.get(base_url+'/bid/content/'+str(biao_id))
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
        
        biao_id=con.back_biaoid(bankname=domain,bidstatus=16,value_way=2,product_type=1)
        if biao_id:
            toubiao()
        else:
            yicixingjinjian.public_yicixing(self)
            toubiao()
            
    def test_toubiao_2(self):
        u"""测试投标后投标人次增加"""
        driver=self.driver
        con=Bankunion_proc()
        def toubiao():
            con=Bankunion_proc()
            biao_id=con.back_biaoid(bankname=domain,bidstatus=16,value_way=2,product_type=1)
            login_bank.login_bank(self,username,password,domain)
            driver.get(base_url+'/bid/content/'+str(biao_id))
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
            
        biao_id=con.back_biaoid(bankname=domain,bidstatus=16,value_way=2,product_type=1)
        if biao_id:
            toubiao()
        else:
            yicixingjinjian.public_yicixing(self)
            toubiao()

    def test_toubiaochaoe(self):
        u"""测试超额投标"""
        driver=self.driver
        con=Bankunion_proc()
        def toubiao():
            con=Bankunion_proc()
            biao_id=con.back_biaoid(bankname=domain,bidstatus=16,value_way=2,product_type=1)
            login_bank.login_bank(self,username,password,domain)
            driver.get(base_url+'/bid/content/'+str(biao_id))
            #跳转到标详情页面
            elements=bank_page.woyaotouzi_tzlb(self)
            #已超额，请重新输入！
            jine=int(return_bidconf('borrowamount'))*10000+100
            elements.get("toubiaojine").send_keys("%s"%jine)
            elements.get("lijitoubiao").click()
            time.sleep(2)
            chaoetishi = driver.find_element_by_css_selector("table.aui_dialog tbody tr td.aui_main div.aui_content").text
            self.assertEqual(u"已超额，请重新输入！", chaoetishi, u"超额投标失败")
            time.sleep(1)
        biao_id=con.back_biaoid(bankname=domain,bidstatus=16,value_way=2,product_type=1)
        if biao_id:
            toubiao()
        else:
            yicixingjinjian.public_yicixing(self)
            toubiao()            


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__=='__main__':
    unittest.main()
