#encoding=utf-8
'''
Created on 2016年5月21日

@author: Administrator
'''

import unittest
import threading 
import time
from HTMLTestRunner import HTMLTestRunner
from conf import bankconf
#加载测试文件


# from bank_part1.test_help_availability import test_help_availability
# from bank_part1.test_bidlist_availability import test_bidlist_availability
# from bank_part1.test_passport_availability import test_passport_availability
from bank_part1.test_all import  test_all
from selenium.common.exceptions import NoSuchElementException
# from bank_omscase.test_jinjian import bank_url


#构建测试集
suite = unittest.TestSuite()
  
# suite.addTest(Index_avaliability_Test("test_all_href"))
# suite.addTest(Index_avaliability_Test("test_all_css"))
# suite.addTest(Index_avaliability_Test("test_all_img"))
# suite.addTest(Index_avaliability_Test("test_all_js"))
 
# suite.addTest(test_help_availability("test_all_href"))
# suite.addTest(test_help_availability("test_all_css"))
# suite.addTest(test_help_availability("test_all_img"))
# suite.addTest(test_help_availability("test_all_js"))
#  
# suite.addTest(test_bidlist_availability("test_all_href"))
# suite.addTest(test_bidlist_availability("test_all_css"))
# suite.addTest(test_bidlist_availability("test_all_img"))
# suite.addTest(test_bidlist_availability("test_all_js"))
#  


# suite.addTest(my_account("test_my_safe"))
# suite.addTest(my_account("test_my"))

class login:
    username = ''
    password = ''
    
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
    
    def login_bank(self,baseurl):
        driver = self.driver
        driver.get(baseurl+"/passport/login")
        elements=self.login_page(self)
        #elements.get("lijidenglu").click()
    
        elements.get("usernamekuang").send_keys(self.username)
        elements.get("passwordkuang").send_keys(self.password)
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
       


class timer(threading.Thread):
    def __init__(self,base_url,fp):
        threading.Thread.__init__(self)  
        self.base_url = base_url  
        self.fp = fp
        
    def run(self):
        runner = HTMLTestRunner(
                            stream=fp,
                            title=self.base_url+u'首页非200测试',
                            description=u'用例执行情况:'
                            )
        test_all.BASE_URL = self.base_url 
        suite.addTest(test_all("test_all_href"))
        suite.addTest(test_all("test_all_css"))
        suite.addTest(test_all("test_all_img"))
        suite.addTest(test_all("test_all_js"))
        runner.run(suite)   

#执行测试
if __name__=='__main__':  
    #按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    #定义报告存放路径
    filename = 'C:\\' + now +'result.html'
    fp = file(filename,'wb')
    #定义测试报告
    runner = HTMLTestRunner(
                            stream=fp,
                            title=self.base_url+u'首页非200测试',
                            description=u'用例执行情况:'
                            )
    test_all.BASE_URL = bankurl
    suite.addTest(test_all("test_all_href"))
    suite.addTest(test_all("test_all_css"))
    suite.addTest(test_all("test_all_img"))
    suite.addTest(test_all("test_all_js"))
#     for key,baseurl in bankconf.urls.items():
#         thread = timer(baseurl,fp)
#         thread.start()
#         time.sleep(1)
    fp.close()
#    unittest.main()   







