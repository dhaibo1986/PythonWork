#!/usr/bin/python
#-*-coding:utf-8-*-

#root=os.path.abspath(os.path.join(os.path.dirname(__file__),))
#sys.path.insert(0,root)
#conf_path=sys.path[0]+"/bank.ini"

urls={
"whccb":"http://test.whccb.com",#威海
"nccbank":"http://test.nccbank.com", #南昌
"syrcbank":"http://test.syrcbank.com",# 泗阳
"yrcfpt":"http://test.yrcfpt.cccb.cn",#长春
"ksrcb":"http://test.ksrcb.com",#昆山
"jzbank":"http://test.jzbank.com",#晋中
"efabank":"http://test.tlrcb.efabank.com", #铜陵
"yqccb":"http://test.yqccb.com", #阳泉
"bgzchina":"http://test.bgzchina.com", #贵州
"taccb":"http://test.taccb.com.cn",# 泰安
"fyydrcb":"http://test.fyydrcb.com",# 颍东
"lidubank":"http://test.lidubank.com", #黎都
"dxalrcb":"http://test.dxalrcb.com", # 大兴安岭
"peiziqianbao":"http://cxyr.peiziqianbao.com",#聚金汇神
"fyyqrcb":"http://test.fyyqrcb.com",#颍泉
"ybccb":"http://nzbank.ybccb.com",#哪吒
"haijinshe":"https://test.haijinshe.com.cn", #海金社
'lccb':'http://test.lccb.com.cn',#廊坊
'sxxrcb':'http://test.sxxrcb.com'

}
bank_map={
   "http://test.whccb.com":"http://www.whccb.com/",
   "http://test.lidubank.com":"http://www.lidubank.com/",
   "http://test.dxalrcb.com":"http://www.dxalrcb.cn/index.php",
   "https://test.haijinshe.com.cn":"https://test.haijinshe.com.cn"
}


def back_link(url):
    bank_url=bank_map.get(url,"")
    return bank_url

username="15900000000"
password="qwe123"

new_username="15900000001"
new_password="qwe123"

domain='jzbank'


def return_bidconf(info):
    jinjian={
    #借款金额
    'borrowamount':'5',
    #借款期限单位1天2月  一次还本息可配置，按月的写死为月
    'borrowunit':'1',
    #借款期限一次性还本息
    'borrowlimit_yici':'30',
    #借款期限按月还本and按月等额
    'borrowlimit_anyue':'3',
    #借款总成本
    'borrowdegression':'12.33',
    #筹款利率
    'borrowRate':'10.31',
     }
    return jinjian.get(info,'')

#db配置
DBHOST='192.168.1.20'
DBNAME='bank_union'
DBUSERNAME='mysqladmin'
DBUSERPASSWD='123465'
DBPORT=3306


    

def bank_url(domain):
    bank_url = urls.get(domain)
    return bank_url


def oms_userinfo():
    username="admin"
    password="admin"
    return username,password
def oms_url():
    base_url="http://%s:6005/login"%DBHOST
    return base_url
