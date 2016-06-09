#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
import unittest, time
import datetime
import sys
sys.path.append("..")
from selenium.common.exceptions import NoSuchElementException
from bank_omscase import login_oms
from page_element import jiaoyiguanli 
from conf.bankconf import *
from conf.db_conf import Bankunion_proc
bank_url = bank_url()
import requests

class Tjsbid_test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote("http://172.17.2.136:3344/wd/hub",webdriver.DesiredCapabilities.FIREFOX)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        #self.base_url = "http://www.bankoms.com"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_tjsbid(self):
        u"""天交所票据进件及终定""" 
        str_json='''{"productDescription":"【产品说明】本产品为天津金融资产交易所挂牌的收益权转让产品，您在购买时需要先注册成为天津金融资产交易所的会员或注册投资者。本产品起购金额为5000元，购买前请认真阅读《产品合约》、《产品说明书》等相关文件，当您“确认付款”则表示您已确认并同意《产品合约》、《产品说明书》等相关文件中的内容。","no":"3",
        "monetaryUnit":"156","productRiskI":"【风险提示】 本产品为约定收益产品，投资有风险，详情请您参考《产品说明书》。","productType":"SCP_ZQSYQ",
        "productContractID":"SFH(JZ)(HHJZ)201500201001_contract.html","issuerCType":"1","issuerBankA":"77230154740007480","riskAssessmentTables":"",
        "underDate":"%(underDate)s","productBreathDay":"%(productBreathDay)s","productEIn":"【收益说明】本产品约定年化收益率为6.5。本产品根据投资人持有产品的实 际天数计算收益, 产品到期日不计息。本产品认购期间内认购资金不享受收益。 ",
        "productBNRiskRating":"1","productQAgeUpperL":"","lowestRiskAScore":"24","issuer":"天津智通慧达资产管理有限公司",
        "fileName":"/home/testspace/bank_ticket/tjs/splitTxt/CPGP-XXXX-20150801-2.txt","productRiskLevel":"M","minRaiseSuccessAmount":"75000",
        "productRDocuments5":"","productQAgeLowerL":"","linesAFRate":"","registerDate":"%(registerDate)s","issuerCity":"天津市","guaranteedAIRate":"%(guaranteedAIRate)s",
        "issuerInstitution":"TJFAE_888888","unitPriceAmount":"%(unitPriceAmount)s","issuerASign":"1","reserved4":"","productDueDate":"%(productDueDate)s",
        "reserved2":"","reserved3":"","reserved1":"","productDeadline":"64","productCode":"SFH(JZ)(HHJZ)201500201","earningsCountType":"1",
        "expectedAYield":"%(expectedAYield)s","issuerCe":"30057952-8","salesAmount":"%(salesAmount)s","productCodeSon":"001","raiseAmount":"%(raiseAmount)s","productRDocuments3":"",
        "productName":"天津金融资产交易所“京诚宝”2015年第2期第1款002号集合债权支持类收益分享合约产品","productsToHonour":"%(productsToHonour)s",
        "productRDocuments4":"","issuerAOBank":"上海浦东发展银行天津科技支行","allowsSecMarketTrading":"1","productRDocuments1":"","earningsType":"1",
        "issuerProvince":"天津","productTermUnit":"D","productRDocuments2":""}''' % {'underDate':'20160310-240000','registerDate':'20160308-162000',
                'productDueDate':'20160409','productsToHonour':'20160412','productBreathDay':'20160312','unitPriceAmount':'2000','salesAmount':'5000',
                'raiseAmount':'80000','guaranteedAIRate':'0.67000','expectedAYield':'0.67000'}
        
        url = 'http://%s:6005/hdb/autoSuperScript/save'%dbhost
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=str_json, headers=headers)
        self.assertEqual(r.text, '00000000', "tjs_bid_post_success")
 
        #进入oms终定审核tjs标
        driver=self.driver
        login_oms.login(self)
        time.sleep(2)
        jiaoyiguanli_ele="ul#menu.nav li.menu:nth-child(2) a.menu"
        driver.find_element_by_css_selector(jiaoyiguanli_ele).click()
        driver.switch_to_frame("menuFrame")
        time.sleep(3)
        #点击借款管理
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/a").click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#collapse169.accordion-body div.accordion-inner ul.nav li:nth-child(2) a.lh001").click()
        time.sleep(2)
        con=Bankunion_proc()
        biao_id=con.back_biaoid('lccb')
        if biao_id is None:
            time.sleep(5)
            con=Bankunion_proc()
            biao_id=con.back_biaoid('lccb')
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
        
    def test_gerenyi_jinzhongxindai(self):
        u"""个人进件晋中信贷"""
        refundway = 1
        driver=self.driver
        login_oms.login(self)
        #交易管理
        time.sleep(1)
        jiaoyiguanli_ele="ul#menu.nav li.menu:nth-child(2) a.menu"
        driver.find_element_by_css_selector(jiaoyiguanli_ele).click()
        #默认为进件录入，直接切换iframe
        #driver.switch_to_frame("mainFrame")
        #定位进件渠道
        time.sleep(2)
        elements=jiaoyiguanli.jinjianluru(self)
        time.sleep(2)
        jinjianqudao="div.controls select#borrowSource.input-medium"
        driver.find_element_by_css_selector(jinjianqudao).find_element_by_css_selector("select#borrowSource.input-medium option[value='%s']"%'jzbank').click()
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
            driver.find_element_by_css_selector("input#borrowTitlePre.input-medium").send_keys(u"晋中信贷")
            driver.find_element_by_css_selector("div#borrowTitleBtnDiv input#borrowTitleOkBtn.btn").click()
            driver.find_element_by_css_selector('input#borrowTitleSeq.input-medium').clear()
            driver.find_element_by_css_selector('input#borrowTitleSeq.input-medium').send_keys(1)
        else:
            driver.find_element_by_css_selector("input#borrowTitlePre.input-medium").send_keys(u"晋中信贷")
            driver.find_element_by_css_selector("div#borrowTitleBtnDiv input#borrowTitleOkBtn.btn").click()
            driver.find_element_by_css_selector('input#borrowTitleSeq.input-medium').send_keys(1)
        time.sleep(3)
        #借款金额
        elements[1].send_keys(borrowamount)
        
        #借款产品类型
        driver.find_element_by_css_selector(" div.control-group div.controls select#productType.input-mini").find_element_by_css_selector("option[value='4']").click()
        js='document.getElementById("trustValueDate").removeAttribute("readonly")'
        driver.execute_script(js)
        time.sleep(10)
        datenow=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        driver.find_element_by_css_selector(' div.controls input#trustValueDate.input-small').send_keys('%s'%datenow)
        
        #借款期限
        driver.find_element_by_css_selector(' div.controls select#borrowPeriodUnit.input-mini').find_element_by_css_selector("option[value='1']").click()
        elements[2].send_keys(borrowlimit_yici)
        #筹标期限
        elements[3].send_keys(7)
        #还款方式
        huankuanfangshi=driver.find_element_by_css_selector("div.control-group div.controls select#refundWay.input-mini")
        #还款方式  一次性还本息
        huankuanfangshi.find_element_by_css_selector("option[value='%s']"%refundway).click()
         
        #借款总成本
        driver.find_element_by_css_selector("div.controls input#borrowDegression.input-medium").send_keys(str(borrowdegression))
        #筹款利率
        driver.find_element_by_css_selector("div.controls input#borrowRate.input-medium").send_keys(str(borrowRate))
         
        time.sleep(1)
        driver.find_element_by_css_selector("input#btnNextStep.btn").click()
        time.sleep(3)

        #终定选择页面
        #table#contentTable.table tbody tr td a.status[bid='309']
        con=Bankunion_proc()
        biao_id=con.back_biaoid(domain)
        while 1:
            try:
                zhongding=driver.find_element_by_css_selector("table#contentTable.table tbody tr td a.status[bid='%s']"%biao_id)
                break
            except NoSuchElementException:
                time.sleep(3)
                break
        zhongding.click()
        time.sleep(1)
        
        #refundwayname=driver.find_element_by_xpath("/html/body/form/table[2]/thead/tr[4]/th[2]").text
        #self.assertEqual(u"按月付息到期还本", refundwayname, u"还款方式错误")
        #点击批核按钮
        driver.find_element_by_css_selector("form#inputForm.form-horizontal div input[type='radio'][value='1']").click()
        #点击保存按钮
        driver.find_element_by_css_selector("div.form-actions input#btnSubmit.btn").click()
        time.sleep(1)
        driver.switch_to_default_content()
        time.sleep(1)
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
        
        
    def test_gerenyi_xinshoubiao(self):
        u"""个人进件晋中新手标"""
        refundway = 1
        driver=self.driver
        #driver.get(self.base_url)
        login_oms.login(self)
        #交易管理
        time.sleep(1)
        jiaoyiguanli_ele="ul#menu.nav li.menu:nth-child(2) a.menu"
        driver.find_element_by_css_selector(jiaoyiguanli_ele).click()
        #默认为进件录入，直接切换iframe
        #driver.switch_to_frame("mainFrame")
        #定位进件渠道
        time.sleep(2)
        elements=jiaoyiguanli.jinjianluru(self)
        time.sleep(2)
        jinjianqudao="div.controls select#borrowSource.input-medium"
        driver.find_element_by_css_selector(jinjianqudao).find_element_by_css_selector("select#borrowSource.input-medium option[value='%s']"%'jzbank').click()
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
            driver.find_element_by_css_selector("input#borrowTitlePre.input-medium").send_keys(u"晋中新手标")
            driver.find_element_by_css_selector("div#borrowTitleBtnDiv input#borrowTitleOkBtn.btn").click()
            driver.find_element_by_css_selector('input#borrowTitleSeq.input-medium').clear()
            driver.find_element_by_css_selector('input#borrowTitleSeq.input-medium').send_keys(1)
        else:
            driver.find_element_by_css_selector("input#borrowTitlePre.input-medium").send_keys(u"晋中新手标")
            driver.find_element_by_css_selector("div#borrowTitleBtnDiv input#borrowTitleOkBtn.btn").click()
            driver.find_element_by_css_selector('input#borrowTitleSeq.input-medium').send_keys(1)
         
        time.sleep(3)
        #借款金额
        elements[1].send_keys(borrowamount)
        #借款产品类型
        driver.find_element_by_css_selector(" div.control-group div.controls select#productType.input-mini").find_element_by_css_selector("option[value='2']").click()

        #借款期限
        driver.find_element_by_css_selector(' div.controls select#borrowPeriodUnit.input-mini').find_element_by_css_selector("option[value='1']").click()
        elements[2].send_keys(borrowlimit_yici)
        #筹标期限
        elements[3].send_keys(7)
        #还款方式
        huankuanfangshi=driver.find_element_by_css_selector("div.control-group div.controls select#refundWay.input-mini")
        #还款方式  一次性还本息
        huankuanfangshi.find_element_by_css_selector("option[value='%s']"%refundway).click()
         
        #借款总成本
        driver.find_element_by_css_selector("div.controls input#borrowDegression.input-medium").send_keys(str(borrowdegression))
        #筹款利率
        driver.find_element_by_css_selector("div.controls input#borrowRate.input-medium").send_keys(str(borrowRate))
         
        time.sleep(1)
        driver.find_element_by_css_selector("input#btnNextStep.btn").click()
        time.sleep(5)

        #终定选择页面
        #table#contentTable.table tbody tr td a.status[bid='309']
        con=Bankunion_proc()
        biao_id=con.back_biaoid('jzbank')
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
        self.assertEqual(u"一次性还本息", refundwayname, u"还款方式错误")
        #点击批核按钮
        driver.find_element_by_css_selector("form#inputForm.form-horizontal div input[type='radio'][value='1']").click()
        #js清除readonly属性
        #js='document.getElementById("publishDate").removeAttribute("readonly");'
        #driver.execute_script(js)
        #time.sleep(2)
        #上线时间
        #onlinetime=datetime.datetime.now()+  datetime.timedelta(hours = 1)
        #onlinetime=onlinetime.strftime('%Y-%m-%d %H:%M:%S')
        #driver.find_element_by_css_selector("div.controls input#publishDate.input-medium").send_keys("%s"%onlinetime)
        #点击保存按钮
        driver.find_element_by_css_selector("div.form-actions input#btnSubmit.btn").click()
        time.sleep(1)
        driver.switch_to_default_content()
        time.sleep(1)
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

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
          
if __name__=="__main__":
    unittest.main()    
        
        
        
