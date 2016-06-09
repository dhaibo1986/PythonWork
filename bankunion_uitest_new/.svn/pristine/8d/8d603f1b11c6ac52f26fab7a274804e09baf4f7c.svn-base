#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium.common.exceptions import NoSuchElementException
import time
import sys
sys.path.append("..")
import login_oms
from page_element import jiaoyiguanli 
from conf.bankconf import return_bidconf,bank_url,domain
from conf.db_conf import Bankunion_proc

bank_url = bank_url(domain)
print domain

def public_yicixing(self):

    u"""个人进件一次性"""
    print 'yicixing'
    refundway = 1
    driver=self.driver
    #driver.get(self.base_url)
    login_oms.login(self)
    #交易管理
    time.sleep(2)
    jiaoyiguanli_ele="ul#menu.nav li.menu:nth-child(2) a.menu"
    driver.find_element_by_css_selector(jiaoyiguanli_ele).click()
    #默认为进件录入，直接切换iframe
    #driver.switch_to_frame("mainFrame")
    #定位进件渠道
    time.sleep(2)
    elements=jiaoyiguanli.jinjianluru(self)
    time.sleep(2)
    jinjianqudao="div.controls select#borrowSource.input-medium"
    driver.find_element_by_css_selector(jinjianqudao).find_element_by_css_selector("select#borrowSource.input-medium option[value='%s']"%domain).click()
    #点击公司or个人
    driver.find_element_by_css_selector("div.control-group div.controls input[value='person']").click()
    
    elements[0][1].send_keys(u"自动化测试")
    elements[0][2].send_keys('320701197905145687')
    elements[0][3].send_keys("15300000000")
    elements[0][4].send_keys(u"测试")
    
    #点击实名认证按钮
    driver.find_element_by_css_selector("div.controls input#btnCheckIdCard.btn").click()
    time.sleep(3)
    driver.switch_to_alert().accept()

    #借款信息
    biaoti_display=driver.find_element_by_css_selector("div#borrowTitleInputDiv div#borrowTitlePreDiv").is_displayed()
    if not biaoti_display:
        driver.find_element_by_css_selector(" div.control-group div.controls div#borrowTitleEditDiv a").click()
        driver.find_element_by_css_selector("input#borrowTitlePre.input-medium").clear()
        driver.find_element_by_css_selector("input#borrowTitlePre.input-medium").send_keys(u"一次性还本息")
        driver.find_element_by_css_selector("div#borrowTitleBtnDiv input#borrowTitleOkBtn.btn").click()
        driver.find_element_by_css_selector('input#borrowTitleSeq.input-medium').clear()
        driver.find_element_by_css_selector('input#borrowTitleSeq.input-medium').send_keys(1)
    else:
        driver.find_element_by_css_selector("input#borrowTitlePre.input-medium").send_keys(u"一次性还本息")
        driver.find_element_by_css_selector("div#borrowTitleBtnDiv input#borrowTitleOkBtn.btn").click()
        driver.find_element_by_css_selector('input#borrowTitleSeq.input-medium').send_keys(1)
    
    #借款金额
    elements[1].send_keys(return_bidconf('borrowamount'))
    #起息方式
    driver.find_element_by_css_selector('div.controls select#valueWay.input-mini').find_element_by_css_selector("option[value='2']").click()
    #借款期限
    driver.find_element_by_css_selector(' div.controls select#borrowPeriodUnit.input-mini').find_element_by_css_selector("option[value='%s']"%return_bidconf('borrowunit')).click()
    elements[2].send_keys(return_bidconf('borrowlimit_yici'))
    #筹标期限
    elements[3].send_keys(7)
    #还款方式
    huankuanfangshi=driver.find_element_by_css_selector("div.control-group div.controls select#refundWay.input-mini")
    #还款方式  一次性还本息
    huankuanfangshi.find_element_by_css_selector("option[value='%s']"%refundway).click()
    
    #借款总成本
    driver.find_element_by_css_selector("div.controls input#borrowDegression.input-medium").send_keys(str(return_bidconf('borrowdegression')))
    #筹款利率
    driver.find_element_by_css_selector("div.controls input#borrowRate.input-medium").send_keys(str(return_bidconf('borrowRate')))
     
    time.sleep(1)
    driver.find_element_by_css_selector("input#btnNextStep.btn").click()
    time.sleep(10)
    
    #终定选择页面
    #table#contentTable.table tbody tr td a.status[bid='309']
    con=Bankunion_proc()
    biao_id=con.back_biaoid(bankname=domain,bidstatus=10)
    if biao_id is None:
        time.sleep(5)
        con=Bankunion_proc()
        biao_id=con.back_biaoid(bankname=domain,bidstatus=10)
    while 1:
        try:
                zhongding=driver.find_element_by_css_selector("table#contentTable.table tbody tr td a.status[bid='%s']"%biao_id)
                break
        except NoSuchElementException:
                time.sleep(3)
    zhongding.click()
    time.sleep(1)
    refundwayname=driver.find_element_by_xpath("/html/body/form/table[2]/thead/tr[4]/th[2]").text
    self.assertEqual(u"一次性还本息", refundwayname, u"还款方式错误")
    #点击批核按钮
    driver.find_element_by_css_selector("form#inputForm.form-horizontal div input[type='radio'][value='1']").click()
    #点击保存按钮
    driver.find_element_by_css_selector("div.form-actions input#btnSubmit.btn").click()
    #driver.switch_to_frame("")
    driver.switch_to_default_content()
    time.sleep(2)
    ntime=0
    while 1:
        try:
            driver.find_element_by_css_selector("div#jbox-state-state0.jbox-state div.jbox-button-panel button.jbox-button[value='ok']").click()
            break
        except NoSuchElementException:
            time.sleep(2)
        ntime+=2
        if ntime>10:
            break
    time.sleep(2) 