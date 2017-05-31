class DataHandler:
	'''
	项目点单位的数据操作
	'''
	dataWraps = set()
	def getDataWrapByLcc(self,lccCode):
		for dataWrap in self.dataWraps:
			if lccCode==dataWrap.lccCode:
				return dataWrap
	
	
	def setDataWrapByLcc(self,dataWrap):
		self.dataWraps.add(dataWrap)
	
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
	