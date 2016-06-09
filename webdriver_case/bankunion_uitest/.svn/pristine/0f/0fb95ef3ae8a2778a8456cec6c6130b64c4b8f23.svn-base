#!/usr/bin/python
# -* - coding: UTF-8 -* -

from selenium import webdriver


def home_page(self):
    driver=self.driver
    #lijidenglu=driver.find_element_by_css_selector("div.r-info a[href='/passport/login']")
    #mianfeizhuce=driver.find_element_by_css_selector("div.r-info a[href='/passport/userCenter/register']")
    bank_link=driver.find_element_by_css_selector(" h1.m-logo a:nth-child(1)")
    shouye=driver.find_element_by_css_selector("a.homepage")
    woyaotouzi=driver.find_element_by_css_selector("nav#m-nav.m-nav a[href='/bid/list']")
    woyaojiekuan=driver.find_element_by_css_selector("nav#m-nav.m-nav a[href='/loan/apply']")
    wodezhanghu=driver.find_element_by_css_selector("a.my[href='/my']")
    bangzhuzhongxin=driver.find_element_by_css_selector("nav#m-nav.m-nav a.help")
    #toubiaoanniu=driver.find_elements_by_css_selector(" li span.c7 a.tender-btn")
    
    d={
    "bank_link":bank_link,
    "shouye":shouye,
    "woyaotouzi":woyaotouzi,
    "woyaojiekuan":woyaojiekuan,
    "wodezhanghu":wodezhanghu,
    "bangzhuzhongxin":bangzhuzhongxin,
    #"toubiaoanniu":toubiaoanniu,
       }
    return d
def login_page(self):
    driver=self.driver
    usernamekuang=driver.find_element_by_css_selector("li.cf input.username")
    passwordkuang=driver.find_element_by_css_selector("li.cf input.password")
    dengluanniu=driver.find_element_by_css_selector("li input.normalBBtn[type='submit']")
    
    d={
    "usernamekuang":usernamekuang,
    "passwordkuang":passwordkuang,
    "dengluanniu":dengluanniu,
       }
    return d

def woyaotouzi_tzlb(self):
    driver=self.driver
    wodeyue=driver.find_element_by_css_selector(" span#yi span#memberyue")
    toubiaojine=driver.find_element_by_css_selector("div.inputFrame input#toubiaojine")
    lijitoubiao=driver.find_element_by_css_selector("li input#toubiao.tb-btn[type='button']")
    #quedinganniu=driver.find_element_by_css_selector("div.aui_buttons button.aui_state_highlight[type='button']")
    #toubiaojilu=driver.find_element_by_css_selector("h3.bright span#count").text
    
    d={
    "wodeyue":wodeyue,
    "toubiaojine":toubiaojine,
    "lijitoubiao":lijitoubiao,
    #"toubiaojilu":toubiaojilu,
    }
    return d

def woyaojiekuan(self):
    driver=self.driver
    tongyi=driver.find_element_by_css_selector(" div.agreeAgreement span")
    huoquyanzhengma=driver.find_element_by_css_selector("li.cf input[type=button]")
    yanzhengma=driver.find_element_by_css_selector(" ul li.cf input[name='code']")
    suozaidiqu=driver.find_element_by_css_selector(" li.cf input.cInput[name='address']")
    daikuanjine=driver.find_element_by_css_selector(" li.cf input.cInput[name=amount]")
    yueshu=driver.find_element_by_css_selector("span#borrowPeriod.cur-val")
    sangeyue=driver.find_element_by_css_selector("ul.select_add li a[name='1']")
    tijiaoshenqing=driver.find_element_by_css_selector("li.sub input.normalBBtn")
    d={
        "tongyi":tongyi,
        "huoquyanzhengma":huoquyanzhengma,
        "yanzhengma":yanzhengma,
        "suozaidiqu":suozaidiqu,
        "daikuanjine":daikuanjine,
        "yueshu":yueshu,
        "sangeyue":sangeyue,
        "tijiaoshenqing":tijiaoshenqing,
    }
    return d
