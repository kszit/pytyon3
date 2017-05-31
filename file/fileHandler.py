# -*- coding:utf-8 -*-
from dataModel import DataHandler
from dataModel import DataWrap


def findError(errorMsg):
	allErrorCount = 0
	for threadName,lines in threadNameToLines.items():
		print(threadName)
		errorcount = 0
		for line in lines:
			if errorMsg in line:
				errorcount = errorcount+1
				allErrorCount = allErrorCount+1
				print(line)
		print(errorcount)
	print(allErrorCount)



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


'''
result = open('./uqs_result.txt','w')
#按照线程整理数据，并输出到文件中			
for threadName in threadNameSet:
	result.write(threadName+"\n")
	isInNoMpp3Line = False
	isFindThreadLine = False
	preLineHasThreadName = False
	for line in allLines:
		if threadName in line:
			result.write(line)
			isFindThreadLine = True
			preLineHasThreadName = True
		else:
			if preLineHasThreadName:
				if not 'mpp3' in line:
					isInNoMpp3Line = True
				if 'mpp3' in line:
					isInNoMpp3Line = False
					preLineHasThreadName = False
				if isInNoMpp3Line:
					result.write(line)

result.close()	
'''

threadNameToLines = dict()
#将分组好的数据放到map中			
for threadName in threadNameSet:
	linesOfThread = list()
	isInNoMpp3Line = False
	isFindThreadLine = False
	preLineHasThreadName = False
	for line in allLines:
		if threadName in line:
			linesOfThread.append(line)
			isFindThreadLine = True
			preLineHasThreadName = True
		else:
			if preLineHasThreadName:
				if not 'mpp3' in line:
					isInNoMpp3Line = True
				if 'mpp3' in line:
					isInNoMpp3Line = False
					preLineHasThreadName = False
				if isInNoMpp3Line:
					linesOfThread.append(line)
		
	threadNameToLines[threadName]=linesOfThread

	

# 按照线程查找错误，并输出错误的关键信息(输出 'insert data error' 对应的信息)
#findError('insert data error')

# 按照线程查找错误，并输出错误的关键信息(输出 'answer not exist' 对应的信息)
#findError('answer not exist')

# 按照线程查找错误，并输出错误的关键信息(输出 'idNumber not exist' 对应的信息)
#findError('idNumber not exist')


#对按照线程分组后的数据，进行处理
dataHandler = DataHandler()
for threadName,lines in threadNameToLines.items():
	for line in lines:
		#查找出每个项目点需要需要处理的数据个数
		if 'need insert' in line:
			lccCode = line[98:102]
			count = line[line.find('--')+2:len(line)]
			dataWrap = dataHandler.getDataWrapByLcc(lccCode)
			if not dataWrap:
				dataWrap = DataWrap()
				dataWrap.threadName = threadName
				dataWrap.lccCode = lccCode
				dataHandler.setDataWrapByLcc(dataWrap)
			dataWrap.needInsertCount = count

			
#输出数据：查看处理结果是否正确			
for dataWrap in dataHandler.dataWraps:
	print(dataWrap.lccCode+":inserCount="+dataWrap.needInsertCount)
	
	
print('结束--文件处理')


