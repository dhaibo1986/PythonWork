#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
import unittest, time
import datetime
import sys
sys.path.append("..")
from selenium.common.exceptions import NoSuchElementException
from public import login_oms
from conf.bankconf import bank_url,DBHOST
from conf.db_conf import Bankunion_proc
bank_url = bank_url('lccb')
import requests

class Tjsbid_test(unittest.TestCase):
    remoteip='http://172.17.2.136:3344/wd/hub'
    def setUp(self):
        self.driver=webdriver.Remote("%s"%self.remoteip,webdriver.DesiredCapabilities.FIREFOX)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        #self.base_url = "http://www.bankoms.com"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_tjsbid(self):
        u"""天交所票据进件及终定""" 
        #起息日
        productBreathDay =  (datetime.datetime.now() +  datetime.timedelta(days = 3)).strftime('%Y%m%d')
        #兑付日
        productsToHonour = (datetime.datetime.now() +  datetime.timedelta(days = 32)).strftime('%Y%m%d')
        #到期日
        productDueDate = (datetime.datetime.now() +  datetime.timedelta(days = 31)).strftime('%Y%m%d')
        #下架日期
        underDate = '%s-240000'%(datetime.datetime.now() +  datetime.timedelta(days = 1)).strftime('%Y%m%d')
        #上架日期
        registerDate = '%s-010000'%datetime.datetime.now().strftime('%Y%m%d')
        
        str_json='''{"productDescription":"【产品说明】本产品为天津金融资产交易所挂牌的收益权转让产品，您在购买时需要先注册成为天津金融资产交易所的会员或注册投资者。本产品起购金额为5000元，购买前请认真阅读《产品合约》、《产品说明书》等相关文件，当您“确认付款”则表示您已确认并同意《产品合约》、《产品说明书》等相关文件中的内容。","no":"3",
        "monetaryUnit":"156","productRiskI":"【风险提示】 本产品为约定收益产品，投资有风险，详情请您参考《产品说明书》。","productType":"SCP_ZQSYQ",
        "sumAmount":"2251165","productContractID":"SFH(JZ)(HHJZ)201500201001_contract.html","issuerCType":"1","issuerBankA":"77230154740007480","riskAssessmentTables":"",
        "underDate":"%(underDate)s","productBreathDay":"%(productBreathDay)s","productEIn":"【收益说明】本产品约定年化收益率为6.5。本产品根据投资人持有产品的实 际天数计算收益, 产品到期日不计息。本产品认购期间内认购资金不享受收益。 ",
        "productBNRiskRating":"1","productQAgeUpperL":"","lowestRiskAScore":"24","issuer":"天津智通慧达资产管理有限公司",
        "fileName":"/home/testspace/bank_ticket/tjs/splitTxt/CPGP-XXXX-20150801-2.txt","productRiskLevel":"M","minRaiseSuccessAmount":"75000",
        "productRDocuments5":"","productQAgeLowerL":"","linesAFRate":"","registerDate":"%(registerDate)s","issuerCity":"天津市","guaranteedAIRate":"%(guaranteedAIRate)s",
        "issuerInstitution":"TJFAE_888888","unitPriceAmount":"%(unitPriceAmount)s","issuerASign":"1","reserved4":"","productDueDate":"%(productDueDate)s",
        "reserved2":"","reserved3":"","reserved1":"","productDeadline":"64","productCode":"SFH(JZ)(HHJZ)201500201","earningsCountType":"1",
        "expectedAYield":"%(expectedAYield)s","issuerCe":"30057952-8","salesAmount":"%(salesAmount)s","productCodeSon":"001","raiseAmount":"%(raiseAmount)s","productRDocuments3":"",
        "productName":"天津金融资产交易所“京诚宝”2015年第2期第1款002号集合债权支持类收益分享合约产品","productsToHonour":"%(productsToHonour)s",
        "productRDocuments4":"","issuerAOBank":"上海浦东发展银行天津科技支行","allowsSecMarketTrading":"1","productRDocuments1":"","earningsType":"1",
        "issuerProvince":"天津","productTermUnit":"D","productRDocuments2":""}''' % {'underDate':underDate,'registerDate':registerDate,
                'productDueDate':productDueDate,'productsToHonour':productsToHonour,'productBreathDay':productBreathDay,'unitPriceAmount':'2000','salesAmount':'5000',
                'raiseAmount':'81234','guaranteedAIRate':'0.067000','expectedAYield':'0.067000'}
        
        url = 'http://%s:6005/hdb/autoSuperScript/save'%DBHOST
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=str_json, headers=headers)
        print r.text
        self.assertEqual(r.text, '00000000', "tjs_bid_post_success")
 
        #进入oms终定审核tjs标
        driver=self.driver
        login_oms.login(self)
#        time.sleep(2)
#        driver.switch_to_default_content()
        time.sleep(3)
        jiaoyiguanli_ele="ul#men u.nav li.menu:nth-child(2) a.menu"
        driver.find_element_by_css_selector(jiaoyiguanli_ele).click()
        driver.switch_to_frame("menuFrame")
        time.sleep(3)
        #点击借款管理
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/a").click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#collapse169.accordion-body div.accordion-inner ul.nav li:nth-child(2) a.lh001").click()
        time.sleep(2)
        con=Bankunion_proc()
        biao_id=con.back_biaoid(bankname='lccb',bidstatus=10)
        if biao_id is None:
            time.sleep(5)
            con=Bankunion_proc()
            biao_id=con.back_biaoid(bankname='lccb',bidstatus=10)
        driver.switch_to_default_content()
        driver.switch_to_frame("mainFrame")
        while 1:
            try:
                zhongding=driver.find_element_by_css_selector("table#contentTable.table tbody tr td a.status[bid='%s']"%biao_id)
                break
            except NoSuchElementException:
                time.sleep(3)
                break
        zhongding.click()
        time.sleep(1)
        refundwayname=driver.find_element_by_xpath("/html/body/form/table[2]/thead/tr[4]/th[2]").text
        self.assertEqual(u"到期一次性还本付息", refundwayname, u"还款方式错误")
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
        time.sleep(3)  
      
     

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
          
if __name__=="__main__":
    unittest.main()    
        
        
        
