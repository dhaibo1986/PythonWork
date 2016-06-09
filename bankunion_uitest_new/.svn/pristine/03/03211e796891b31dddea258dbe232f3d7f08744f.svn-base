#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
sys.path.append("..")
from conf import bankconf
#import ConfigParser
#===============================================================================
# base_dir=sys.argv[0]
# dir2=os.path.dirname(base_dir)
# dir3=dir2.strip("bank_websitecase\public")
# dir4=dir3+'\conf\oms_info.ini'
#conf.read(dir4)
#===============================================================================
omsusername,omspassword = bankconf.oms_userinfo()


def login(self):
    driver = self.driver
    base_url=bankconf.oms_url()
    driver.get(base_url)
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(omsusername)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(omspassword)
    driver.find_element_by_css_selector("form#loginForm.form-signin input.btn").click()
