#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time, sys
sys.path.append("..")
from public import login_bank
from conf import bankconf
from page_element import bank_page
import traceback

base_url=bankconf.bank_url()
username_input,password =bankconf.userinfo()

class Home_link(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote("http://172.17.2.136:3344/wd/hub",webdriver.DesiredCapabilities.FIREFOX)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.base_url = base_url
        self.verificationErrors = []
        self.accept_next_aler = True
        
    def test_home_link(self):
        u"""判断银行首页跳转银行页是否正确"""
        driver=self.driver
        driver.get(self.base_url)
        link_url=bankconf.back_link(base_url)
        now_window=driver.current_window_handle
        elements=bank_page.home_page(self)
        elements.get("bank_link").click()
        if link_url == self.base_url:
            return True        
        time.sleep(2)
        all_windows=driver.window_handles
        current_url=""
        for window in all_windows:
            if window !=now_window:
                driver.switch_to_window(window)
                time.sleep(5)
                current_url=driver.current_url

        self.assertEqual(current_url, link_url, u"跳转失败") 

    def test_bank_login(self):
        u"""验证银行登录"""
        driver=self.driver
        login_bank.login_bank(self)
        #dis=driver.find_element_by_xpath("/html/body/div[1]").is_displayed()
        username=driver.find_element_by_css_selector("div.account a#userid").text
        self.assertIn(username_input, username, u"登录失败")

    def test_zhanghaocuowu(self):
        u"""测试账号密码错误用户登录"""
        driver = self.driver
        driver.get(self.base_url+"/passport/login")
        elements=bank_page.login_page(self)

        elements.get("usernamekuang").send_keys("19911111111")
        elements.get("passwordkuang").send_keys("qwe123")
        elements.get("dengluanniu").click()
        zhanghaocuowu = driver.find_element_by_css_selector("table.aui_dialog tbody tr td.aui_main div.aui_content").text
        time.sleep(2)
        self.assertEqual(u"账号或密码错误!", zhanghaocuowu,u"错误账号登录")        

    def test_message(self):
        u"""message页面是否正常"""
        driver = self.driver
        login_bank.login_bank(self)
        time.sleep(2)
        driver.find_element_by_css_selector("a#msg_warp.msg_warp i.fa").click()
        xitongtongzhi = driver.find_element_by_css_selector("div.mainContent div.h-title h3").text
        self.assertEqual(u"系统通知", xitongtongzhi, u"系统通知页面异常")
        
    def test_register(self):
        u"""注册页面是否正常"""
        driver = self.driver
        driver.get(self.base_url+"/passport/userCenter/register")
        try:
            driver.find_element_by_xpath("//div[2]/div/form/ul/li[1]/input")
        except NoSuchElementException:
            self.assertFalse(u"注册页面失败",u"注册页面失败")

    def test_home(self):
        u"""首页非500"""
        driver=self.driver
        driver.get(self.base_url)
        try:
            driver.find_element_by_css_selector("div.before form.loginFormFn ul li input.normalBtn")
        except NoSuchElementException:
            self.verificationErrors.append(str(traceback.format_exc()))


        

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__=='__main__':
    unittest.main()
