#!/usr/bin/env python
#-*-coding:utf-8-*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class hdb_login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote("http://172.19.2.136:3344/wd/hub",webdriver.DesiredCapabilities.FIREFOX)
        self.driver=webdriver.Remote("http://172.19.2.136:3344/wd/hub",webdriver.DesiredCapabilities.FIREFOX)
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.haodaibao.com"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_hdb_login(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys("13716850263")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123465")
        driver.find_element_by_css_selector("input.normalBtn").click()
        self.assertEqual("testphone2", driver.find_element_by_link_text("testphone2").text)
        driver.find_element_by_link_text("testphone2").click()
        self.assertEqual("testphone2", driver.find_element_by_css_selector("a.accountname").text)
        driver.find_element_by_link_text(u"[退出]").click()
        self.assertEqual(u"登录", driver.find_element_by_link_text(u"登录").text)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
