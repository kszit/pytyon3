# -*- coding:utf-8 -*-

'''
使用 threadpool,

需要安装：
pip install threadpool
'''

import threadpool
import time

def mytask(param):
	print('task'+str(param))
	time.sleep(4)

data = [1,3,4,6,7]
pool = threadpool.ThreadPool(10)
requests = threadpool.makeRequests(mytask,data)

for req in requests:
	pool.putRequest(req)
	
pool.wait()

