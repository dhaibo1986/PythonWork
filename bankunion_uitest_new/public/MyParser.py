#encoding=utf-8
'''
Created on 2016年5月21日

@author: Administrator
'''

import HTMLParser
from conf import bankconf
from conf.bankconf import domain
 

class MyParser(HTMLParser.HTMLParser):  
    
    BASE_URL = bankconf.bank_url(domain)

    def __init__(self):  
        HTMLParser.HTMLParser.__init__(self) 
        self.links = set([])
        self.css = set([])
        self.img = set([])
        self.js = set([])

    def handle_starttag(self, tag, attrs):  
        # 这里重新定义了处理开始标签的函数  
        if tag == 'a':  
            # 判断标签<a>的属性  
            for name,value in attrs:  
                if name == 'href'  :  
                    if value.find('syslogout') <= 0:
                        if value.startswith('http'):
                            self.links.add(value)
                        elif value.startswith('/'):
                            self.links.add(self.BASE_URL+value)
        elif tag == 'link' :
            for name,value in attrs:  
                if name == 'href'  :  
                    self.css.add(value) 
        elif tag == 'img':
            for name,value in attrs:
                if name == 'src'   :
                    if value.startswith('http'):
                        self.img.add(value)
                    elif value.startswith('/'):
                        self.img.add(self.BASE_URL+value)
        elif tag == 'script':
            for name,value in attrs:
                if name == 'src':
                    self.js.add(value)                    




