#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from page_element import bank_page
from conf import bankconf
bank_url = bankconf.bank_url()
username,password = bankconf.userinfo()

def login_bank(self):
    driver = self.driver
    driver.get(bank_url+"/passport/login")
    elements=bank_page.login_page(self)
    #elements.get("lijidenglu").click()

    elements.get("usernamekuang").send_keys(username)
    elements.get("passwordkuang").send_keys(password)
    elements.get("dengluanniu").click()
    
    dis=driver.find_element_by_xpath("/html/body/div[1]").is_displayed()
    if dis:
        time.sleep(1)
        driver.find_element_by_css_selector("button.aui_state_highlight").click()
        time.sleep(1)
    else:
        try:
            driver.find_element_by_css_selector("button.aui_state_highlight").click()
        except NoSuchElementException:
            pass
    #username=driver.find_element_by_css_selector("div.account a#userid").text

    