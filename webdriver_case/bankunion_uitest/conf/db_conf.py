#!/usr/bin/python
#-*-coding:utf-8-*-
import MySQLdb
import MySQLdb.cursors
import sys
sys.path.append("..")
from conf.bankconf import *
import time

class Bankunion_proc(object):
    def __init__(self):
        self.conn=MySQLdb.Connect(host=dbhost,user=dbusername,passwd=dbuserpasswd,db=dbname,port=dbport,\
                cursorclass=MySQLdb.cursors.DictCursor,charset="utf8")


    def create_proc(self):
        cursor=self.conn.cursor()
        clear_db_sql="""CREATE PROCEDURE cleardb()
            BEGIN
            delete from audit_bid_info;
            delete from hdb_risk_fund;
            delete from member_refund_info;
            delete from member_request_bid;
            delete from member_borrow_contract_info;
            delete from member_loan_stat;
            delete from member_account where m_id not in(-100);
            delete from member_base_info;
            delete from member_borrow_stat;
            delete from member_data_auth;
            delete from member_job_info;
            delete from member_linkman_info;
            delete from hdb_bid_fund;
            delete from hdb_income_fund;
            delete from member_buy_bid;
            delete from member_fund_detail;
            delete from member_oper_log;
            delete from hdb_recharge_info;
            delete from member_bid_refund;
            delete from member_bid_info_param;
            delete from member_buy_bid;
            delete from member_pwd_modify;
            delete from member_card_info;
            delete from member_cash_info;
            delete from hdb_withdraw_deposit_factorage;
            delete from member_realname_auth;
            delete from member_request_bid_count;
            delete from member_refund_total_info;
            delete from member_refund_log;
            delete from member_refund_detail;
            delete from member_recharge_order;
            delete from member_recharge_info;
            delete from member_order;
            delete from member_mobile_code;
            delete from member_cash_pay;
            delete from member_bid_describe;
            delete from hdb_withdraw_deposit;
            delete from hdb_sys_msg;
            delete from hdb_notice;
            delete from hdb_mobile_pay;
            delete from member where id!=-100;
            delete from member_bid_info;
            delete from quick_borrow;
            update hdb_account_info set recharge_factorage=0.00,risk_fund=0.00,bid_fund=0.00,income_fund=0.00,withdraw_deposit=0.00,withdraw_deposit_factorage=0.00,debt_fund=0.00;
            END;"""
        
        cursor.execute("select `name` from mysql.proc where db = '%s' and `type` = 'PROCEDURE'"%dbname)
        proc_name = cursor.fetchone()
        if proc_name:
            if proc_name['name'] == 'cleardb': 
                print u"cleardb is exist"
        else:
            cursor.execute(clear_db_sql)
            self.conn.commit()       
        time.sleep(2)
            
    def clear_and_createdata(self):
        cursor=self.conn.cursor()   #游标
        #清理数据库
        cursor.execute("call cleardb;")
        self.conn.commit()
        #前端实名认证用户插库
        realname_insert='insert member_realname_auth (real_name,id_card,status) values ("实名用户","441602199309234817",1)'
        #天交所票据进件用户实名认证
        realname_ticket='insert member_realname_auth (real_name,id_card,status) values ("天交所用户","510704199609282269",1)'
        cursor.execute(realname_insert)
        cursor.execute(realname_ticket)
        self.conn.commit()
        real_id_sql="select id from member_realname_auth where id_card = '441602199309234817'"
        real_id_ticket="select id from member_realname_auth where id_card = '510704199609282269'"
        cursor.execute(real_id_sql)
        real_id=cursor.fetchone()
        cursor.execute(real_id_ticket)
        real_ticket_id=cursor.fetchone()

        domain='select domain from sys_bank;'
        cursor.execute(domain)
        bankapps=cursor.fetchall()
        bankapp=[]
        for bank in bankapps:
            bankapp.append(bank['domain'])
        for bankdomain in bankapp:
            member='''insert into member (uname,pwd,trade_pwd,mobile_phone,purpose,source,province,city,is_agree,auth_id,is_locked,is_withhold,point,error_cnt,create_date,auth_status,update_times,register_platform,identity,be_invite_code,FORBID_LOGIN_STATUS,FORBID_LOGIN_EXPIRE_DATE) values('15900000000', '33c0dfd61383db51b45c0a9e29e94b772f827d425f0490c235e8edac', '33c0dfd61383db51b45c0a9e29e94b772f827d425f0490c235e8edac', '15900000000', '0', '1', '0', '0', '1', '%s', '0', '0', '0', '0', '2015-09-16 09:37:48', '0', '0', '%s', '0', null, '0', null)'''%(real_id['id'],bankdomain)
            cursor.execute(member)
        #插入天交所用户
        member_ticket='''insert into member (uname,pwd,trade_pwd,mobile_phone,purpose,source,province,city,is_agree,auth_id,is_locked,is_withhold,point,error_cnt,create_date,auth_status,update_times,register_platform,identity,be_invite_code,FORBID_LOGIN_STATUS,FORBID_LOGIN_EXPIRE_DATE) values('15300000001', '33c0dfd61383db51b45c0a9e29e94b772f827d425f0490c235e8edac', '33c0dfd61383db51b45c0a9e29e94b772f827d425f0490c235e8edac', '15300000001', '0', '1', '0', '0', '1', '%s', '0', '0', '0', '0', '2015-09-16 09:37:48', '0', '0', 'lccb', '0', null, '0', null)'''%(real_ticket_id['id'])
        cursor.execute(member_ticket)
        #插入晋中新手标投标用户
        new_jzbakmember='''insert into member (uname,pwd,trade_pwd,mobile_phone,purpose,source,province,city,is_agree,auth_id,is_locked,is_withhold,point,error_cnt,create_date,auth_status,update_times,register_platform,identity,be_invite_code,FORBID_LOGIN_STATUS,FORBID_LOGIN_EXPIRE_DATE) values('15900000001', '33c0dfd61383db51b45c0a9e29e94b772f827d425f0490c235e8edac', '33c0dfd61383db51b45c0a9e29e94b772f827d425f0490c235e8edac', '15900000001', '0', '1', '0', '0', '1', '%s', '0', '0', '0', '0', '2015-09-16 09:37:48', '0', '0', 'jzbank', '0', null, '0', null)'''%(real_ticket_id['id'])
        cursor.execute(new_jzbakmember)
        self.conn.commit()

        member_id_reg_platform='''select id,register_platform from member where id not in (select m_id from member_account)'''
        cursor.execute(member_id_reg_platform)
        all_m_id=cursor.fetchall()

        for data in all_m_id:
            bankdomain=data['register_platform']
            m_id=data['id']
            insert_account='''insert into member_account (m_id,usable_amount,bank_app) values ('%s','5000000','%s')'''%(m_id,bankdomain)
            cursor.execute(insert_account)
        self.conn.commit()
        #查询天交所进件用户id
        tjs_member_id="""select id from member where mobile_phone='15300000001' and register_platform='lccb'"""
        cursor.execute(tjs_member_id)
        tjs_mem_id=cursor.fetchone()
        #配置字典表天交所进件用户
        insert_tjsuser="""update sys_dict set value='%s' where type='member_param' """%tjs_mem_id['id']
        set_seq="update sequence set seq_no=0 where seq_type='titleNum'"
        cursor.execute(insert_tjsuser)
        cursor.execute(set_seq)
        self.conn.commit()
        cursor.close()
        self.conn.close()
        
    def back_random_code(self,mobile_phone):
        cur=self.conn.cursor()
        cur.execute("select random_code from member_mobile_code where mobile_phone=%s order by create_date desc limit 1",(mobile_phone))
        code=cur.fetchone()
        return code["random_code"]
    
    def back_biaoid(self,bankname):
        cur=self.conn.cursor()
        time.sleep(2)
        cur.execute("SELECT m_bid from audit_bid_info where bank_app='%s' and global_status='10' ORDER BY id desc limit 1"%bankname)
        bid_id=cur.fetchone()
        return bid_id['m_bid']
        

if __name__=="__main__":
    con=Bankunion_proc()
    con.create_proc()
    con.clear_and_createdata()
