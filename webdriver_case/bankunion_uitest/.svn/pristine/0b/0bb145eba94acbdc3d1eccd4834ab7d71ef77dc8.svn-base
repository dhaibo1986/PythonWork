#!/usr/bin/python
#-*-coding:utf-8-*-
import unittest
import HTMLTestRunner
import os ,time,datetime
import sys
sys.path.append("..")
from conf.db_conf import Bankunion_proc
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import email.MIMEBase
global dirs
#dirs=os.getcwd()
dirs=sys.path[0]

def ready_db():
    con=Bankunion_proc()
    con.create_proc()
    con.clear_and_createdata()

def createsuit():
    casedirs=[]
    casedirs.append(dirs+'/bank_omscase')
    casedirs.append(dirs+'/bank_websitecase')
    suite=[]
    testunit1=unittest.TestSuite()
    discover1=unittest.defaultTestLoader.discover(casedirs[0],pattern ='test_*',top_level_dir=None)
    for case_suite in discover1:
        testunit1.addTest(case_suite)
    suite.append(testunit1)
    
    testunit2=unittest.TestSuite()
    discover2=unittest.defaultTestLoader.discover(casedirs[1],pattern ='test_*',top_level_dir=dirs)
    for case_suite in discover2:
        testunit2.addTest(case_suite)
    suite.append(testunit2)
    return suite,casedirs

def sentmail(file_new):
#发信邮箱
    mail_from='qa@qianbao.com'
#收信邮箱
    mail_to=['lidx@qianbao.com']
#定义正文
    main_msg = MIMEMultipart()
    text_msg = MIMEText("bankunion_uitest_report")
    main_msg.attach(text_msg) 
    
    contype = 'application/octet-stream'  
    maintype, subtype = contype.split('/', 1) 

    f = open(file_new, 'rb')
    file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
    file_msg.set_payload(f.read()) 
    f.close()
    email.Encoders.encode_base64(file_msg)
    
    basename = os.path.basename(file_new)  
    file_msg.add_header('Content-Disposition',  
    'attachment', filename = basename)  
    main_msg.attach(file_msg)
    #msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    main_msg['From'] = "<qa@qianbao.com>"
    main_msg['To'] = ",".join( mail_to )
#定义标题
    main_msg['Subject'] = u"Bannkunion_UItest_report"
#定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    main_msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')

    smtp=smtplib.SMTP()
#连接 SMTP 服务器，
    smtp.connect('smtp.exmail.qq.com',port=25)
#用户名密码
    smtp.login('qa@qianbao.com','test123465')
    smtp.sendmail(mail_from,mail_to,main_msg.as_string())
    smtp.quit()
    print 'email send seccess'

def sendreport():
    datenow=time.strftime('%y%m%d',time.localtime(time.time()))
    result_dir = dirs+'/report/'+datenow+'/'
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"/"+fn)\
        if not os.path.isdir(result_dir+"\\"+fn) else 0)
    print 'new report is ',lists[-1]
    file_new = os.path.join(result_dir,lists[-1])
    sentmail(file_new)


if __name__=='__main__':
    ready_db()
    suite,casedir=createsuit()
    now=time.strftime('%H%M%S',time.localtime(time.time()))
    datenow=time.strftime('%y%m%d',time.localtime(time.time()))
    repdir=dirs+'/report/'+datenow
    if os.path.exists(repdir):
        pass
    else:
        os.makedirs(repdir)
    
    html=repdir+'/'+"bankunion"+datenow+'_'+now+'.html'
    fp = file(html,'wb')
    n=0
    for i in suite:
        runner=HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=casedir[n].split('/')[-1]+u'Bankunion测试报告',
            description=None)
        runner.run(i)
        n+=1
    fp.close()
    sendreport() 
