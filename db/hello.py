# -*-coding:utf-8 -*-
import cx_Oracle
import os 
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8' 
con = cx_Oracle.connect('scm/develop@10.24.10.224/bdcor5')
cur = con.cursor()
cur.execute('select name from sys_account')
for result in cur:
	print(result[0])
	
cur.close()
con.close()

