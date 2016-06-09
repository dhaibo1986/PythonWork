#!/usr/bin/python
# -* - coding: UTF-8 -* -
from selenium import webdriver
import time

def jinjianluru(self):
    driver=self.driver
    time.sleep(2)
    driver.switch_to_frame("mainFrame")
    print "switch mainframe"
    #定位交易渠道银行
    #jinjianqudao=driver.find_element_by_css_selector("div.controls select#borrowSource.input-medium").find_element_by_css_selector("select#borrowSource.input-medium option[value='%s']")
    #公司名称
    #gongsiname=driver.find_element_by_css_selector("div.controls input#compName.input-medium")
    #融资人信息 从公司名称 到项目联系人手机号 7组元素
    rongzirenxinxi=driver.find_elements_by_css_selector("div#companyDiv div.control-group div.controls input.input-medium")
    #借款金额
    jiekuanjine=driver.find_element_by_css_selector("div.controls input#borrowAmount.input-medium")
    #借款总成本
    #jiekuanzongchengben=driver.find_element_by_css_selector("div.controls input#borrowDegression.input-medium")
    #筹款利率
    #choukuanlilv=driver.find_element_by_css_selector("div.controls input#borrowRate.input-medium")
    #借款期限
    jiekuanqixian=driver.find_element_by_css_selector("div.controls input#borrowLimit.input-medium")
    #筹款期限
    choukuanqixian=driver.find_element_by_css_selector("div.controls input#bidDeadline.input-medium")
    
    #臭婊期限
    choubiaoqixian=driver.find_element_by_css_selector("div.controls input#bidDeadline.input-medium")
    lists=[rongzirenxinxi,jiekuanjine,jiekuanqixian,choukuanqixian,choubiaoqixian]
    return lists