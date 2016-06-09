#!/usr/bin/python
#-*-coding:utf-8-*-
import unittest
import HTMLTestRunner
import os ,time
import sys
from unittest.suite import TestSuite
sys.path.append("..")
sys.path.append('./bank_case/')
from conf.db_conf import Bankunion_proc
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from unittest import TestLoader
from unittest import case
from unittest import getTestCaseNames
import email.MIMEBase
import multiprocessing
import threading
global dirs
#dirs=os.getcwd()
dirs=sys.path[0]

def ready_db():
    con=Bankunion_proc()
    con.create_proc()
    con.clear_and_createdata()

def createsuit():
    casedirs=[]
    casedirs.append(dirs+'/bank_case')
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

def SelectSort(num):
    for i in range(0,len(num)):
        mindex=i
        for j in range(i,len(num)):
            if [x for x in num[mindex].values()][0]>[x for x in num[j].values()][0]:
                mindex=j
        num[mindex],num[i]=num[i],num[mindex]
    return num

def back_list(d):
    li=[]
    if not isinstance(d,dict):  
        return [] 
    for i,j in d.iteritems():
        li.append({i:j})
    return li
def backcaselist(dirs):
    caselist=[]
    for modle in os.listdir(dirs):
        if ('test' in modle) and modle.endswith('.py'):
            caselist.append(modle.split('.')[0])
    return caselist


def creat():
    loadcase=TestLoader()
    testsuite=[]
    suite1=TestSuite()
    suite2=TestSuite()
    caseclass_dict={}
    def backcount(d):
        n=0
        for i in d.values():
            n+=i
        return n
    def caseclass_count(caselist):
        print 'dir caselist',caselist
        for casename in caselist:
            module=loadcase._get_module_from_name(casename)
            for name in dir(module):
                obj = getattr(module,name)
                if isinstance(obj, type) and issubclass(obj, case.TestCase):
                    modeltestcases_list=getTestCaseNames(obj,'test')
                    caseclass_dict[obj]=len(modeltestcases_list)
        return caseclass_dict
    classcase_dict=caseclass_count(backcaselist(dirs+'/bank_case'))
    
    case_and_count_list=back_list(classcase_dict)
    sort_case=SelectSort(case_and_count_list)
    print sort_case
    for i in range(len(sort_case)):
        if i%2==0:
            suite1.addTest(loadcase.loadTestsFromTestCase([x for x in sort_case[i].keys()][0]))
            [x for x in sort_case[i].keys()][0].remoteip='http://172.17.2.136:3344/wd/hub'
        else:
            suite2.addTest(loadcase.loadTestsFromTestCase([x for x in sort_case[i].keys()][0]))
            [x for x in sort_case[i].keys()][0].remoteip='http://172.17.2.57:3344/wd/hub'
    
    print 'suite1',suite1
    print 'suite2',suite2
    testsuite.append(suite1)
    testsuite.append(suite2)
    return testsuite
    
    #===========================================================================
    # 
    # casecount=backcount(classcase_dict)
    # nn=casecount/2
    # countn=0
    # for caseclass,count in caseclass_dict.iteritems():
    #     countn+=count
    #     if countn < nn:
    #         caseclass.remoteip='http://172.17.2.136:3344/wd/hub'
    #         suite1.addTest(loadcase.loadTestsFromTestCase(caseclass))
    #     else:
    #         caseclass.remoteip='http://172.17.2.57:3344/wd/hub'
    #         suite2.addTest(loadcase.loadTestsFromTestCase(caseclass))
    # testsuite=[]
    # print 'suite1',suite1
    # print 'suite2',suite2
    # testsuite.append(suite1)
    # testsuite.append(suite2)
    # return testsuite
    #===========================================================================

if __name__=='__main__':
    ready_db()
    #suite,casedir=createsuit()
    suite = creat()
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
    proclist=[]
    for i in suite:
        runner=HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            #title=casedir[n].split('/')[-1]+u'Bankunion测试报告',
            title=u'bankunion_report',
            description=None)
        proc = threading.Thread(target=runner.run,args=(i,))
        proclist.append(proc)
        #runner.run(i)
        print 'proc',proc
        n+=1
    for i in range(2):
        proclist[i].start()
    for i in range(2):
        proclist[i].join()
    fp.close()
    sendreport() 
