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

result = open('./uqs_result.txt','w')
#按照线程整理数据，并输出到文件中			
for threadName in threadNameSet:
	result.write(threadName+"\n")
	isInNoMpp3Line = False
	isFindThreadLine = False
	for line in allLines:
		if threadName in line:
			result.write(line)
			isFindThreadLine = True
		if isFindThreadLine:
			if line.find('mpp3')==-1:
				isInNoMpp3Line = True
			if line.find('mpp3')!=-1:
				isInNoMpp3Line = False
			if isInNoMpp3Line:
				result.write(line)

result.close()	

print('结束--文件处理')

