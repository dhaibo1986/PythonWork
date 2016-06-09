#!/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
import unittest, time
import datetime
import sys
sys.path.append("..")
import re
from selenium.common.exceptions import NoSuchElementException
from public import login_oms
from page_element import jiaoyiguanli 
from conf.bankconf import username,password,bank_url,return_bidconf,new_username,new_password,oms_url
from public import login_bank
from page_element import bank_page
from conf.db_conf import Bankunion_proc
import requests
bank_url = bank_url('jzbank')
baseoms_url=oms_url()

valueDate =  (datetime.datetime.now() +  datetime.timedelta(days = 2)).strftime('%Y-%m-%d')
toDate =  (datetime.datetime.now() +  datetime.timedelta(days = 33)).strftime('%Y-%m-%d')
        

class Jzbank_test(unittest.TestCase):
    remoteip='http://172.17.2.136:3344/wd/hub'
    def setUp(self):
        self.driver=webdriver.Remote("%s"%self.remoteip,webdriver.DesiredCapabilities.FIREFOX)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.base_url = baseoms_url
        self.verificationErrors = []
        self.accept_next_alert = True
    
    
    def test_jzxintuo(self):
        u"""个人晋中信托进件"""
        refundway = 1
        driver=self.driver
        login_oms.login(self)
        #交易管理
        time.sleep(1)
        jiaoyiguanli_ele="ul#menu.nav li.menu:nth-child(2) a.menu"
        driver.find_element_by_css_selector(jiaoyiguanli_ele).click()
        #默认为进件录入，login_omse
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
        elements[1].send_keys(return_bidconf('borrowamount'))
        
        #借款产品类型
        driver.find_element_by_css_selector(" div.control-group div.controls select#productType.input-mini").find_element_by_css_selector("option[value='4']").click()
        js1='document.getElementById("valueDate").removeAttribute("readonly")'
        js2='document.getElementById("toDate").removeAttribute("readonly")'
        driver.execute_script(js1)
        time.sleep(1)
        driver.execute_script(js2)
        time.sleep(5)
        #起息日期为当前日期加两天
        driver.find_element_by_css_selector('div div.controls input#valueDate.input-small').send_keys('%s'%valueDate)
        
        #到期日期
        driver.find_element_by_css_selector('div div.controls input#toDate.input-small').send_keys('%s'%toDate)
        #借款期限
        driver.find_element_by_css_selector('div.controls input#borrowLimitTjs.input-medium').click()
        #筹标期限
        elements[3].send_keys(7)
        #还款方式
        huankuanfangshi=driver.find_element_by_css_selector("div.control-group div.controls select#refundWay.input-mini")
        #还款方式  一次性还本息
        huankuanfangshi.find_element_by_css_selector("option[value='%s']"%refundway).click()
         
        #借款总成本
        driver.find_element_by_css_selector("div.controls input#borrowDegression.input-medium").send_keys(str(return_bidconf('borrowdegression')))

        time.sleep(2)
        #筹款利率
        driver.find_element_by_css_selector("div.controls input#borrowRate.input-medium").send_keys(str(return_bidconf('borrowRate')))
         
        time.sleep(1)
        driver.find_element_by_css_selector("input#btnNextStep.btn").click()
        time.sleep(10)

        #终定选择页面
        #table#contentTable.table tbody tr td a.status[bid='309']
        con=Bankunion_proc()
        biao_id=con.back_biaoid(bankname='jzbank',bidstatus=10)
        ntime=0
        while 1:
            try:
                zhongding=driver.find_element_by_css_selector("table#contentTable.table tbody tr td a.status[bid='%s']"%biao_id)
            except NoSuchElementException:
                time.sleep(2)
            ntime+=2
            if ntime>9:
                break
        zhongding.click()
        time.sleep(1)
        
        #refundwayname=driver.find_element_by_xpath("/html/body/form/table[2]/thead/tr[4]/th[2]").text
        #self.assertEqual(u"按月付息到期还本", refundwayname, u"还款方式错误")
        refundwayname=driver.find_element_by_xpath("/html/body/form/table[2]/thead/tr[4]/th[2]").text
        self.assertEqual(u"一次性还本息", refundwayname, u"还款方式错误")
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
        
    def test_jzxindaigudingjinjian(self):
        u"""个人进件晋中信贷固定起息"""
        refundway = 1
        driver=self.driver
        login_oms.login(self)
        #交易管理
        time.sleep(1)
        jiaoyiguanli_ele="ul#menu.nav li.menu:nth-child(2) a.menu"
        driver.find_element_by_css_selector(jiaoyiguanli_ele).click()
        #默认为进件录入，login_omse
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
            driver.find_element_by_css_selector("input#borrowTitlePre.input-medium").send_keys(u"晋中固定起息")
            driver.find_element_by_css_selector("div#borrowTitleBtnDiv input#borrowTitleOkBtn.btn").click()
            driver.find_element_by_css_selector('input#borrowTitleSeq.input-medium').clear()
            driver.find_element_by_css_selector('input#borrowTitleSeq.input-medium').send_keys(1)
        else:
            driver.find_element_by_css_selector("input#borrowTitlePre.input-medium").send_keys(u"晋中固定起息")
            driver.find_element_by_css_selector("div#borrowTitleBtnDiv input#borrowTitleOkBtn.btn").click()
            driver.find_element_by_css_selector('input#borrowTitleSeq.input-medium').send_keys(1)
        time.sleep(3)
        #借款金额
        elements[1].send_keys(return_bidconf('borrowamount'))
        
        #借款产品类型
        driver.find_element_by_css_selector(" div.control-group div.controls select#productType.input-mini").find_element_by_css_selector("option[value='1']").click()
        driver.find_element_by_css_selector("div.controls select#valueWay.input-mini").find_element_by_css_selector("option[value='1']").click()
        js1='document.getElementById("valueDate").removeAttribute("readonly")'
        js2='document.getElementById("toDate").removeAttribute("readonly")'
        driver.execute_script(js1)
        time.sleep(1)
        driver.execute_script(js2)
        time.sleep(5)
        #起息日期为当前日期加两天
        driver.find_element_by_css_selector('div div.controls input#valueDate.input-small').send_keys('%s'%valueDate)
        
        #到期日期
        driver.find_element_by_css_selector('div div.controls input#toDate.input-small').send_keys('%s'%toDate)
        #借款期限
        driver.find_element_by_css_selector('div.controls input#borrowLimitTjs.input-medium').click()
        #筹标期限
        elements[3].send_keys(7)
        #还款方式
        huankuanfangshi=driver.find_element_by_css_selector("div.control-group div.controls select#refundWay.input-mini")
        #还款方式  一次性还本息
        huankuanfangshi.find_element_by_css_selector("option[value='%s']"%refundway).click()
         
        #借款总成本
        driver.find_element_by_css_selector("div.controls input#borrowDegression.input-medium").send_keys(str(return_bidconf('borrowdegression')))

        time.sleep(2)
        #筹款利率
        driver.find_element_by_css_selector("div.controls input#borrowRate.input-medium").send_keys(str(return_bidconf('borrowRate')))
         
        time.sleep(1)
        driver.find_element_by_css_selector("input#btnNextStep.btn").click()
        time.sleep(10)

        #终定选择页面
        #table#contentTable.table tbody tr td a.status[bid='309']
        con=Bankunion_proc()
        biao_id=con.back_biaoid(bankname='jzbank',bidstatus=10)
        ntime=0
        while 1:
            try:
                zhongding=driver.find_element_by_css_selector("table#contentTable.table tbody tr td a.status[bid='%s']"%biao_id)
            except NoSuchElementException:
                time.sleep(2)
            ntime+=2
            if ntime>9:
                break
        zhongding.click()
        time.sleep(1)
        
        #refundwayname=driver.find_element_by_xpath("/html/body/form/table[2]/thead/tr[4]/th[2]").text
        #self.assertEqual(u"按月付息到期还本", refundwayname, u"还款方式错误")
        refundwayname=driver.find_element_by_xpath("/html/body/form/table[2]/thead/tr[4]/th[2]").text
        self.assertEqual(u"一次性还本息", refundwayname, u"还款方式错误")
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
        time.sleep(5) 
       

        
        
    def test_jzguding_date(self):
        u'''晋中信贷固定起息日前端和投标是否正确'''
        def jinjiantoubiaotest():
            driver=self.driver
            #查找发售中标id
            login_bank.login_bank(self,username,password,'jzbank')
            driver.get(bank_url+'/bid/content/'+str(biao_id))
            time.sleep(1)

            bid_dates=driver.find_element_by_css_selector('div.module-box div#box1.content-area span.interest-period').text
            date_list=re.findall('\d{4}-\d{2}-\d{2}',bid_dates)
            start_date,enddate=con.back_date(biao_id)
            if self.assertEqual(start_date, date_list[0], u'起息日错误'):
                print u'起息日正确' 
            if self.assertEqual(enddate, date_list[1], u'到期日错误'):
                print u'到期日正确'
            
            #标详情页面元素list
            elements=bank_page.woyaotouzi_tzlb(self)
            #投标前投标人数
            toubiao_num_before=int(driver.find_element_by_css_selector("h3.bright span#count").text)
            elements.get("toubiaojine").send_keys("100")
            elements.get("lijitoubiao").click()
            time.sleep(2)
            driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight[type='button']").click()
            time.sleep(2)
            #投标后人投标人数
            toubiao_num_after=int(driver.find_element_by_css_selector("h3.bright span#count").text)
            self.assertEqual(toubiao_num_before+1,toubiao_num_after,u"投标记录未增加")

        con=Bankunion_proc()
        #获取发售中标，如果没有标调用进件方法
        biao_id=con.back_biaoid(bankname='jzbank',bidstatus=16,value_way=1,product_type=1)
        if biao_id:
            jinjiantoubiaotest()
        else:
            self.test_jzxindaigudingjinjian()
            con=Bankunion_proc()
            biao_id=con.back_biaoid(bankname='jzbank',bidstatus=16,value_way=1,product_type=1)
            print 'biaoid',biao_id
            jinjiantoubiaotest()


    def test_new_bid(self):
        u"""个人进件晋中新手标进件投标"""
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
        elements[1].send_keys(return_bidconf('borrowamount'))
        #借款产品类型
        driver.find_element_by_css_selector(" div.control-group div.controls select#productType.input-mini").find_element_by_css_selector("option[value='2']").click()

        #借款期限
        driver.find_element_by_css_selector(' div.controls select#borrowPeriodUnit.input-mini').find_element_by_css_selector("option[value='1']").click()
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
        time.sleep(9)

        #终定选择页面
        #table#contentTable.table tbody tr td a.status[bid='309']
        con=Bankunion_proc()
        biao_id=con.back_biaoid(bankname='jzbank',bidstatus=10)
        ntime=0
        while 1:
            try:
                zhongding=driver.find_element_by_css_selector("table#contentTable.table tbody tr td a.status[bid='%s']"%biao_id)
                break
            except NoSuchElementException:
                time.sleep(2)
            ntime+=2
            if ntime>9:
                break
        zhongding.click()
        time.sleep(1)
        driver.switch_to_default_content()
        time.sleep(1)
        driver.switch_to_frame("mainFrame")
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
        
        
    
        #website
        login_bank.login_bank(self,new_username,new_password,'jzbank')
        driver.get(bank_url+'/bid/content/'+str(biao_id))
        driver.find_element_by_css_selector(' div.leftArea input#toubiaojine.num-amount').send_keys('100')
        driver.find_element_by_css_selector('div.rightCon div.btnWrap input#toubiao.btnFortb').click()
        time.sleep(2)
        tishi = driver.find_element_by_css_selector(' table.aui_dialog tbody tr td.aui_main div.aui_content').text
        self.assertEqual(tishi, u'恭喜您，投标成功！', u'投资新手标失败')
        #点击确定
        driver.find_element_by_css_selector('tr td.aui_footer div.aui_buttons button.aui_state_highlight').click()
        time.sleep(2)
        driver.find_element_by_css_selector(' div.leftArea input#toubiaojine.num-amount').send_keys('100')
        driver.find_element_by_css_selector('div.rightCon div.btnWrap input#toubiao.btnFortb').click()
        tishi = driver.find_element_by_css_selector(' table.aui_dialog tbody tr td.aui_main div.aui_content').text
        self.assertEqual(tishi, u'非首次投标用户，不可以投新手标；请查看其它产品。', u'投资新手标失败')
        time.sleep(2)


    def test_gudingqixi_fuhe(self):
        u'晋中固定起息信贷筹标复核'
        con=Bankunion_proc()
        driver = self.driver 
        def fullbid():
            con=Bankunion_proc()
            biao_id=con.back_biaoid(bankname='jzbank',bidstatus=16,value_way=1,product_type=1)
            loginurl="%s/ajaxlogin"%bank_url
            logindata={'username':'%s'%username,'password':'cXdlMTIz','showcode':''}
            s=requests.Session()
            s.post(url=loginurl,data=logindata,verify=False)
            fullbidurl='%s/memberBidInfo/memberRequestBid'%bank_url
            #需要满标的标id
            bid_enter_amount,approved_amount=con.back_bid_money(bid=biao_id,domain='jzbank')
            toubiaojine=approved_amount - bid_enter_amount
            postdata={'id':'%s'%biao_id,'money':int(toubiaojine),'showCode':'0','resmoney':int(toubiaojine),'number1':"0.2342342342323"}
            r=s.post(url=fullbidurl,data=postdata)
            print r.text
            self.assertEquals('ok', r.text, u'投满标失败')
            time.sleep(2)
            #oms
            
            #login_oms.login(self)
            driver.get(baseoms_url)
            
            #交易管理
            time.sleep(2)
            driver.switch_to_default_content()
            #driver.switch_to_frame("mainFrame")
            jiaoyiguanli_ele="ul#menu.nav li.menu:nth-child(2) a.menu"
            time.sleep(1) 
            driver.find_element_by_css_selector(jiaoyiguanli_ele).click()
            driver.switch_to_frame("menuFrame")
            time.sleep(3)
            #点击借款管理
            driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/a").click()
            time.sleep(1)
            driver.find_element_by_css_selector(' div#collapse169.accordion-body div.accordion-inner ul.nav li:nth-child(3) a.lh001').click()
            driver.switch_to_default_content()
            time.sleep(1)
            driver.switch_to_frame("mainFrame")
            time.sleep(2)
            #点击筹标复核
            driver.find_element_by_css_selector("table#contentTable.table tbody tr td a[href='/hdb/memberBidInfo/toFullScaleReview?id=%s']"%biao_id).click()
            #点击审核通过
            driver.find_element_by_css_selector("div form#inputForm.form-horizontal span label[for='isApproved1']").click()
            driver.find_element_by_css_selector("html body div form#inputForm.form-horizontal textarea#bidRecheckRemark.valid").send_keys('dsafasdasddf')
            #点击投标复核保存
            driver.find_element_by_css_selector("html body div form#inputForm.form-horizontal input#btnSubmit.btn").click()
            time.sleep(2)
            driver.switch_to_default_content()
            time.sleep(1)
            driver.switch_to_frame("menuFrame")
            time.sleep(2)
            
            driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/a').click()
            time.sleep(1)
            #点击还款总表
            driver.find_element_by_css_selector('div#collapse230.accordion-body div.accordion-inner ul.nav li:nth-child(1) a.lh001').click()
            driver.switch_to_default_content()
            time.sleep(1)
            driver.switch_to_frame("mainFrame")
            #定位到对应的标，点击查看
            driver.find_element_by_css_selector('table#contentTable.table tbody tr td a[href="/hdb/memberRefundInfo/detail?bid=%s&flag=1"]'%biao_id).click()
            #获取实际还款日
            huankuanri=driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr/td[6]').text
            start_date,enddate=con.back_date(biao_id)
            self.assertEqual(enddate, huankuanri, u'还款日错误')
            
            
        biao_id=con.back_biaoid(bankname='jzbank',bidstatus=16,value_way=1,product_type=1)
        if biao_id:
            fullbid()
        else:
            self.test_jzxindaigudingjinjian()
            #self.driver.quit()
            fullbid()
        
        

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
          
if __name__=="__main__":
    unittest.main()    
