#!/usr/bin/python
#-*-coding:utf-8-*-
import MySQLdb
import MySQLdb.cursors

conn=MySQLdb.Connect(host='192.168.1.214',user='mysqladmin',passwd='123465',db='bank_union',port=3306,\
    cursorclass=MySQLdb.cursors.DictCursor,charset="utf8")

phone_number=raw_input("输入手机号")
num=raw_input("输入要插入数量")
bankapp=raw_input("输入对应bankapp名称")
num=int(num)
phone_n=int(phone_number)
all_phone=[]
for i in range(num):
    all_phone.append(phone_n)
    phone_n+=1

all_phone_str=str(all_phone).rstrip(']').lstrip('[').replace('L', '')
phone_number=int(phone_number)
sql='''select mobile_phone from member where mobile_phone in (%s) and register_platform="%s"'''%(all_phone_str,bankapp)
cursor=conn.cursor()
cursor.execute(sql)
a=cursor.fetchall()
if not a:
    for i in range(num):
        member='''insert into member (uname,pwd,trade_pwd,mobile_phone,purpose,source,province,city,is_agree,auth_id,is_locked,is_withhold,point,error_cnt,create_date,auth_status,update_times,register_platform,identity,be_invite_code,FORBID_LOGIN_STATUS,FORBID_LOGIN_EXPIRE_DATE) values('%s', '33c0dfd61383db51b45c0a9e29e94b772f827d425f0490c235e8edac', '33c0dfd61383db51b45c0a9e29e94b772f827d425f0490c235e8edac', '%s', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '2015-09-16 09:37:48', '0', '0', '%s', '0', null, '0', null)'''%(phone_number,phone_number,bankapp)
        phone_number+=1
        cursor=conn.cursor()
        cursor.execute(member)
        cursor.close()
        conn.commit()
else:
    a=str(a)
    print "数据库中存在数据%s，不执行插入操作"%a

member_id='''select id from member where id not in (select m_id from member_account)'''
cursor=conn.cursor()
cursor.execute(member_id)
all_m_id=cursor.fetchall()
for m_id in all_m_id:
    insert_account='''insert into member_account (m_id,usable_amount,bank_app) values ('%s','5000000','%s')'''%(m_id['id'],bankapp)
    m_id['id']+=1
    cursor=conn.cursor()
    cursor.execute(insert_account)
    cursor.close()
    conn.commit()

conn.close()

#if __name__=="__main__":
