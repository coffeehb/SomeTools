#encoding=GBK
'''
Created on 2014年10月12日
配置文件
@author: cf_hb
'''
global RHOST
global MaxPic
global FILEPATH
global ThreadNumber


#配置爬行目标入口URL
#形如:RHOST = "http://www.baidu.com/"
RHOST=""

#图片存放目录
FILEPATH = ""
#线程并发数量(默认值:10)
ThreadNumber = 10
#最大爬行图片数量 -1表示不受限制
MaxPic = 0

#爬行文件后缀名
# global TYPES
#之后版本可以手动设置，指定爬行的文件类型。
TYPE = "jpg"
InnerThread = 5

 

