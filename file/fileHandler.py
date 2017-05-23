# -*- coding:utf-8 -*-
print('开始--文件处理')
'''
try:
	f = open('./uqs-info-2017-05-22.log','r',encoding='utf-8')
	print(f.read())
finally:
	if f:
		f.close()
'''

'''
result = open('./uqs_result.txt','w')
result.write('dd')
result.close()
'''


#print('2017-05-22 04:05:26.032 [mpp3-uqsinfo-byLcc-36-exe1] INFO  c.s.b.s.HrToBdcor3_UqsInfoByLcc_Bean - 1506:need insert--106'[25:51])


threadNameSet = set()
allLines = list()
with open('./uqs-info-2017-05-22.log','r',encoding='utf-8') as f:
	allLines = f.readlines()
	
for line in allLines:
	threadName = line[25:51]
	if not threadName.find('mpp3'):
		threadNameSet.add(threadName)

print('线程数:'+str(len(threadNameSet)))

#遍历所有线程			
for threadName in threadNameSet:
	print(threadName)
	for line in allLines:
		if threadName in line:
			print(line)
	
print('结束--文件处理')

