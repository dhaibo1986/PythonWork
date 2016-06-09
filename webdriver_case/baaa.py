# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote("http://172.19.2.136:3344/wd/hub",webdriver.DesiredCapabilities.FIREFOX)
        self.driver=webdriver.Remote("http://172.19.2.136:3344/wd/hub",webdriver.DesiredCapabilities.FIREFOX)
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.214:6005/"
        self.verificationErrors = []
        self.accept_next_alert = True
      

    
    def test_untitled(self):
        driver = self.driver
        driver.get(self.base_url + "/login;jsessionid=7A680A9AC8B37C4CCD7D1F6843468B8C")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_xpath(u"//input[@value='登 录']").click()
        driver.find_element_by_link_text(u"交易管理").click()
        time.sleep(5)
        current_handle = self.driver.current_window_handle
        all_handle = self.driver.window_handles
        for x in all_handle:
            if x != current_handle:
                self.driver.switch_to_window(x)
                break
        driver.find_element_by_xpath("//input[@id='lxName']").send_keys("admin1111111111111")
        js="var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        driver.find_element_by_css_selector("#divMovieContainer > input[type=\"button\"]").click()
        self.assertEqual(u"请选择要上传的文件!", self.close_alert_and_get_its_text())
    
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
