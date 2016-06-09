#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time, sys
sys.path.append("..")
from selenium.common.exceptions import StaleElementReferenceException
from public import login_oms

class Login(unittest.TestCase):
    remoteip='http://172.17.2.136:3344/wd/hub'
    def setUp(self):
        self.driver=webdriver.Remote("%s"%self.remoteip,webdriver.DesiredCapabilities.FIREFOX)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        #self.base_url = "http://www.bankoms.com"
        self.verificationErrors = []
        self.accept_next_alert = True
        #self.base_url=login_oms.base_url
    
    def test_login(self):
        u"""验证登录oms"""
        driver=self.driver
        #driver.get(self.base_url)
        login_oms.login(self)
        #左上角用户登录名称信息  
        page_username="li.dropdown:nth-child(2) a.dropdown-toggle[href='#']"
        admin=u"管理员"
        page_admin=driver.find_element_by_css_selector(page_username).text
        self.assertIn(admin,page_admin,u"用户名错误")
        
    def test_search(self):
        u"oms用户搜索"
        driver=self.driver
        login_oms.login(self)      
        time.sleep(2)
        #定位用户管理菜单栏
        yonghuguanli="div.nav-collapse ul#menu.nav li.menu:nth-child(3) a.menu"
        yonghuguanli_ele=WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector(yonghuguanli))
        yonghuguanli_ele.click()
        time.sleep(2)
        #'swith to mainframe'
        driver.switch_to_frame("mainFrame")
        #查询方式选择框
        xuanzekuang=driver.find_element_by_css_selector("form#searchForm.breadcrumb label select#searchFlag.input-medium")
        xuanzekuang.find_element_by_css_selector("option[value='4']").click()
        driver.find_element_by_id("searchValue").clear()
        driver.find_element_by_id("searchValue").send_keys('15900000000')
        driver.find_element_by_id("btnSubmit").click()
        #查询结果的第一个的用户名/手机号
        user_moblile1="div table#contentTable.table tbody tr:nth-child(1) td:nth-child(1) a"
        #user_moblile1_val=WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector(user_moblile1))
        try:   
            user_moblile1_val=driver.find_element_by_css_selector(user_moblile1).text
        except StaleElementReferenceException:
            time.sleep(2)
            user_moblile1_val=driver.find_element_by_css_selector(user_moblile1).text
        self.assertIn('15900000000',user_moblile1_val,u"查询失败")
        #time.sleep(2)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
