#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
import unittest, time, sys
sys.path.append("..")
from public import login_bank
from conf import bankconf
from page_element import bank_page
from conf.db_conf import Bankunion_proc
username_input,password =bankconf.userinfo()

base_url=bankconf.bank_url()
username_input,password =bankconf.userinfo()

class Woyaojiekuan(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote("http://172.17.2.136:3344/wd/hub",webdriver.DesiredCapabilities.FIREFOX)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.base_url = base_url
        self.verificationErrors = []
        self.accept_next_aler = True
    
    def test_woyaojiekuan(self):
        u"""我要借款"""
        driver=self.driver
        login_bank.login_bank(self)
        elements_home=bank_page.home_page(self)
        elements_home.get("woyaojiekuan").click()
        elements_jiekuan=bank_page.woyaojiekuan(self)
        elements_jiekuan.get("tongyi").click()
        elements_jiekuan.get("huoquyanzhengma").click()
        time.sleep(5)
        yanzhengma=Bankunion_proc().back_random_code(username_input)
        elements_jiekuan.get("yanzhengma").send_keys(yanzhengma)
        elements_jiekuan.get("suozaidiqu").send_keys(u"北京")
        elements_jiekuan.get("daikuanjine").send_keys("1")
        elements_jiekuan.get("yueshu").click()
        elements_jiekuan.get("sangeyue").click()
        elements_jiekuan.get("tijiaoshenqing").click()
        time.sleep(2)
        chenggong=driver.find_element_by_css_selector("tbody tr td.aui_main div.aui_content").text
        self.assertEqual(chenggong, u"成功!", u"借款失败")
        driver.find_element_by_css_selector(" button.aui_state_highlight").click()
        time.sleep(2)
#查询成功借款的sql
# SELECT qb.`name` name,qb.phone phone,qb.borrow_amount borrowAmount,borrow_period borrowPeriod,`status` status,source,su.NAME operName,DATE_FORMAT(qb.CREATE_DATE,'%Y-%m-%d %H:%i:%s ') createDate  ,qb.id id,qb.address address,qb.id_card idcard FROM quick_borrow qb LEFT JOIN sys_user su ON qb.oper_id=su.id  WHERE 1=1  and qb.source  in (1,2,3,4,5,6,7,12,13,14,15,16,17,18,-1)  AND qb.phone=?  ORDER BY qb.create_date DESC       
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__=='__main__':
    unittest.main()
