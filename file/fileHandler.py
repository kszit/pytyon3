# -*- coding:utf-8 -*-
from dataModel import DataHandler
from dataModel import DataWrap
from dataModel import DataOfFile




print('开始--文件处理')
fileName = './uqs-info-2017-05-22.log';

# txt文件数据的封装
dataOfFile = DataOfFile(fileName)

# txt文件处理
dataHandler = DataHandler(dataOfFile)
dataHandler.findData()		

#输出到屏幕
dataHandler.prinfAllData()


print('结束--文件处理')


