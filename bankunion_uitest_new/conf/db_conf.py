#!/usr/bin/python
#-*-coding:utf-8-*-
import MySQLdb
import MySQLdb.cursors
import sys
sys.path.append("..")
from conf.bankconf import *
import time
import datetime

class Bankunion_proc(object):
    def __init__(self):
        self.conn=MySQLdb.Connect(host=DBHOST,user=DBUSERNAME,passwd=DBUSERPASSWD,db=DBNAME,port=DBPORT,\
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
            delete from member_quickpay_sign;
            delete from member_bid_describe;
            delete from member_cash_transfer_detail;
            delete from hdb_withdraw_deposit;
            delete from hdb_sys_msg;
            delete from hdb_notice;
            delete from hdb_mobile_pay;
            delete from member where id!=-100;
            delete from member_bid_info;
            delete from quick_borrow;
            update hdb_account_info set recharge_factorage=0.00,risk_fund=0.00,bid_fund=0.00,income_fund=0.00,withdraw_deposit=0.00,withdraw_deposit_factorage=0.00,debt_fund=0.00;
            END;"""
        
        cursor.execute("select `name` from mysql.proc where db = '%s' and `type` = 'PROCEDURE'"%DBNAME)
        proc_name = cursor.fetchone() 
        if proc_name:
            if proc_name['name'] == 'cleardb': 
                cursor.execute('drop procedure cleardb;')
                self.conn.commit()
                cursor.execute(clear_db_sql)
                self.conn.commit()
                cursor.close()
        else:
            cursor.execute(clear_db_sql)
            self.conn.commit() 
            cursor.close()    
        time.sleep(2)
            
    def clear_and_createdata(self):
        cursor=self.conn.cursor()
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
        #插入晋中新手标投标用户15900000001
        new_jzbakmember='''insert into member (uname,pwd,trade_pwd,mobile_phone,purpose,source,province,city,is_agree,auth_id,is_locked,is_withhold,point,error_cnt,create_date,auth_status,update_times,register_platform,identity,be_invite_code,FORBID_LOGIN_STATUS,FORBID_LOGIN_EXPIRE_DATE) values('15900000001', '33c0dfd61383db51b45c0a9e29e94b772f827d425f0490c235e8edac', '33c0dfd61383db51b45c0a9e29e94b772f827d425f0490c235e8edac', '15900000001', '0', '1', '0', '0', '1', '%s', '0', '0', '0', '0', '2015-09-16 09:37:48', '0', '0', 'jzbank', '0', null, '0', null)'''%(real_ticket_id['id'])
        cursor.execute(new_jzbakmember)
        self.conn.commit()

        member_id_reg_platform='''select id,register_platform from member where id not in (select m_id from member_account)'''
        cursor.execute(member_id_reg_platform)
        all_m_id=cursor.fetchall()
        
        #当前日期
        datenow=datetime.datetime.now().strftime('%Y%m%d')
        #插入线下充值订单时间
        pay_date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #线下充值订单号
        serial_number=datenow+str(int(time.time()))
        int_serial_number=int(serial_number)
        
        for data in all_m_id:
            bankdomain=data['register_platform']
            m_id=data['id']
            int_serial_number+=1
            #账户中存入500000金额
            insert_account='''insert into member_account (m_id,usable_amount,bank_app) values ('%s','5000000','%s')'''%(m_id,bankdomain)
            cursor.execute(insert_account)
            insert_hdb_recharge_info='''INSERT into hdb_recharge_info  (m_id,serial_number,pay_amount,pay_date,pay_bank,receive_bank,status,apply_uid,audit_uid,audit_date,create_date,bank_app)\
             VALUES ('%s','%s','5000000','%s','1','1','4','1','1','%s','%s','%s')'''\
             %(m_id,'DCZ'+str(int_serial_number),pay_date,pay_date,pay_date,bankdomain )
            cursor.execute(insert_hdb_recharge_info) 
            self.conn.commit()
            #插入银行卡信息
            insert_card='''insert into member_card_info (m_id,account_name,bank,bank_simple_code,bank_province,bank_city,bank_name,bank_card,bind_status,is_withhold,is_valid,create_date,web_quickpay,bank_mobile) values\
            ('%s','实名用户','中国工商银行','ICBC','北京市','北京市','中国工商银行股份有限公司北京小汤山支行','6212260200103692998',1,0,1,'%s',1,'15300000001')'''%(m_id,pay_date)
            cursor.execute(insert_card)
            #插入签约信息
            insert_sign='''insert into member_quickpay_sign (customer_no,m_id,sign_req_time,inner_trade_no,trade_source,bank_code,card_type,card_no,holder_name,holder_id_type,holder_id_no,holder_mobile,sign_res_time,sign_res_code,sign_res_desc,sign_type,\
            is_sign_confrim,is_sign_success,trade_amount,bank_app) values ('1000000011','%s','%s','%s','BUPC','ICBC','DC','6213213132132123','suer','IDCARD','512501196406240315','15300000001','%s','00000000','SESSCESS','SP',1,1,100,'%s')'''\
            %(m_id,pay_date,str(int_serial_number),pay_date,bankdomain)
            cursor.execute(insert_sign)
            self.conn.commit()
        #查询天交所进件用户id
        tjs_member_id="""select id from member where mobile_phone='15300000001' and register_platform='lccb'"""
        cursor.execute(tjs_member_id)
        tjs_mem_id=cursor.fetchone()
        #配置字典表天交所进件用户
        insert_tjsuser="""update sys_dict set value='%s' where type='member_param' """%tjs_mem_id['id']
        set_seq="update sequence set seq_no=0 where seq_length='18'"
        cursor.execute(insert_tjsuser)
        cursor.execute(set_seq)
        self.conn.commit()
        cursor.close()
        self.conn.close()
        
    def back_random_code(self,mobile_phone):
        cur=self.conn.cursor()
        cur.execute("select random_code from member_mobile_code where mobile_phone=%s order by create_date desc limit 1",(mobile_phone))
        code=cur.fetchone()
        if code:
            cur.close()
            return code["random_code"]
        else:
            cur.close()
            return None
            
    
    def back_biaoid(self,**kwargs):
        cur=self.conn.cursor()
        time.sleep(2)
        bidstatus=kwargs.get('bidstatus')
        bankname=kwargs.get('bankname')
        value_way=kwargs.get('value_way','')
        product_type=kwargs.get('product_type','')
        #未终定标
        if bidstatus==10:
            cur.execute("SELECT m_bid from audit_bid_info where bank_app='%s' and global_status='10' ORDER BY id desc limit 1"%bankname)
            bid_id=cur.fetchone()
            if bid_id:
                cur.close()
                return bid_id['m_bid']
            
            else:
                cur.close()
                return None
            
        #待发售标
        elif bidstatus==16:
            #信托固定起息日标value_way等于1，product_type=2;信贷固定value_way=1，product_type=1；次日起息信贷value_way=2，product_type=1
            cur.execute("select id from member_bid_info where product_type='%s' and value_way='%s' and id in (select m_bid from audit_bid_info where global_status=16 and bank_app='%s')"%(product_type,value_way,bankname))
            bid_id=cur.fetchone()
            print 'bid',bid_id
            if bid_id:
                cur.close()
                return bid_id['id']
            else:
                cur.close()
                return None

        else:
            return u'status error'
        
    def back_date(self,bid):
        cur=self.conn.cursor()
        print bid
        cur.execute("select value_start_date,value_end_date from member_bid_info where id ='%s'"%bid)
        biddate=cur.fetchone()
        if biddate:
            cur.close()
            return biddate['value_start_date'].strftime('%Y-%m-%d'),biddate['value_end_date'].strftime('%Y-%m-%d')        
        else:
            cur.close()
            return None
        
    def back_needfullbid(self,bankname):
        cur=self.conn.cursor()
        cur.execute("select m_bid from audit_bid_info where bank_app='%s' and global_status='16'"%bankname)
        needfullbid=cur.fetchone()
        if needfullbid:
            cur.close()
            return needfullbid['m_bid']
        else:
            cur.close()
            return None

    def back_bid_money(self,bid,domain):
        cur=self.conn.cursor()
        #已投金额
        cur.execute("select bid_enter_amount from member_bid_info where id = '%s' and bank_app='%s'"%(bid,domain))
        bid_enter_amount=cur.fetchone()
        #终定金额
        cur.execute("select approved_amount from audit_bid_info where m_bid='%s' and bank_app='%s'"%(bid,domain))
        approved_amount=cur.fetchone()
        cur.close()
        return bid_enter_amount['bid_enter_amount'],approved_amount['approved_amount']
   

if __name__=="__main__":
    con=Bankunion_proc()
    con.clear_and_createdata()
