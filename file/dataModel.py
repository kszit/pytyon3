# -*- coding:utf-8 -*-

class DataOfFile:
	'''
	日志文件的封装。
	对日志文件进行了转换，转换后的结果放到字典中，key：线程名称  value：线程对应行的列表
	'''
	allLines = list()
	threadNameSet = set()
	
	def __init__(self,file):
		with open(file,'r',encoding='utf-8') as f:
			self.allLines = f.readlines()
			
		for line in self.allLines:
			threadName = line[25:51]
			if not threadName.find('mpp3'):
				self.threadNameSet.add(threadName)

		self.__groupByThreadName()
		
	def __groupByThreadName(self):
		self.threadNameToLines = dict()
		#将分组好的数据放到map中			
		for threadName in self.threadNameSet:
			linesOfThread = list()
			isInNoMpp3Line = False
			isFindThreadLine = False
			preLineHasThreadName = False
			for line in self.allLines:
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
				
			self.threadNameToLines[threadName]=linesOfThread
		
class DataHandler:
	'''
	项目点单位的数据操作
	'''
	dataWraps = set()
	
	def __init__(self,dataOfFile):
		self.dataOfFile = dataOfFile
	
	# 数据处理
	def findData(self):
		for threadName,lines in self.dataOfFile.threadNameToLines.items():
			for line in lines:
				#查找出每个项目点需要需要处理的数据个数
				dataWrap = self.__findSumCount(line,'need insert','needInsertCount')
				dataWrap = self.__findSumCount(line,'errorCount','errorCount')
				dataWrap = self.__findSumCount(line,'noIdNumberCount','noIdNumberCount')
				dataWrap = self.__findSumCount(line,'noAnswerCount','noAnswerCount')
				dataWrap = self.__findSumCount(line,'insert data error','ORA00001count')
				dataWrap = self.__findSumCount(line,'success','success')
				if dataWrap:
					dataWrap.threadName = threadName
	# 输出数据到屏幕
	def prinfAllData(self):
		for dataWrap in self.dataWraps:
			dataWrap.printCount()
	
	
	def getDataWrapByLcc(self,lccCode):
		for dataWrap in self.dataWraps:
			if lccCode==dataWrap.lccCode:
				return dataWrap
	
	
	def __setDataWrapByLcc(self,dataWrap):
		self.dataWraps.add(dataWrap)
	
	
	def __findSumCount(self,line,codeStr,attr):
		if codeStr in line:
			lccCode = line[98:102]
			if line.rfind('--')!=-1:
				count = int(line[line.rfind('--')+2:len(line)].strip('\n'))
			else:
				count = 1
				
			dataWrap = self.getDataWrapByLcc(lccCode)
			if not dataWrap:
				dataWrap = DataWrap()
				dataWrap.lccCode = lccCode
				self.__setDataWrapByLcc(dataWrap)
			
			try:
				dataWrap.__dict__[attr] = dataWrap.__dict__[attr] + int(count)
			except KeyError:
				dataWrap.__dict__[attr] = int(count)
			
			return dataWrap
	
class DataWrap:
	'''
	每个项目点单位的数据封装
	'''
	threadName = ''
	lccCode = 0
	needInsertCount = 0
	errorCount = 0
	noIdNumberCount = 0
	noAnswerCount = 0
	ORA00001count = 0
	success = 0
	
	def printCount(self):
		print('==========================')
		
		print(self.lccCode)
		print("threadName="+self.threadName)
		print("inserCount="+str(self.__dict__['needInsertCount']))
		print("errorCount="+str(self.errorCount))
		print("noIdNumberCount="+str(self.noIdNumberCount))
		print("noAnswerCount="+str(self.noAnswerCount))
		print("ORA00001count="+str(self.ORA00001count))
		print("success="+str(self.success))

		
	