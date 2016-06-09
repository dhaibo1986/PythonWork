#!/usr/bin/python
# -* - coding: UTF-8 -* -

def menu(self):
    driver=self.driver
    jiaoyiguanli=driver.find_element_by_css_selector("ul#menu.nav li.menu:nth-child(2) a.menu") 
    yonghuguanli=driver.find_element_by_css_selector("div.nav-collapse ul#menu.nav li.menu:nth-child(3) a.menu")
    return [jiaoyiguanli,yonghuguanli]