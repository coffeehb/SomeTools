#encoding=GBK
'''
Created on 2014年10月12日
爬虫主线程
@author: cf_hb
'''

import os
import sys
import shutil

from ImageCrawler import ImageCraw

from CrawlerConfig import MaxPic
from CrawlerConfig import FILEPATH
from CrawlerConfig import ThreadNumber
from CrawlerConfig import RHOST
from CrawlerConfig import TYPE
from CrawlerConfig import InnerThread

# print FILEPATH
#设置默认的图片路径
FILEPATH = os.getcwd()+os.sep+"pics"+os.sep

errMsg=[]

def Building(argvs):
    
    global RHOST
    global ThreadNumber
    global FILEPATH
    global MaxPic
    
    p=0
    while p<len(argvs):
        if "-n" == argvs[p]:
#           print "设置线程数量"
            ThreadNumber = argvs[p+1]
            p = p + 1
            continue
        if "-l"==argvs[p]:
#                 print "设置最大图片爬行数量"
            MaxPic = argvs[p+1]
            p = p + 1
            continue
        if "-o"==argvs[p]:
#                 print "设置路径"
            FILEPATH = argvs[p+1]
            p = p + 1
            continue
        if "-t"==argvs[p]:
#                 print "设置爬行目标"
            RHOST = argvs[p+1]
            p = p + 1
            continue
        p = p + 1
            
def ParamAnalysis():
    global errMsg
    global RHOST
    global ThreadNumber
    global FILEPATH
    global MaxPic
    
    print RHOST
    print ThreadNumber
    print FILEPATH
    print MaxPic
    
    if len(sys.argv)==1:
        with open("help.txt",'r')as f:
            for line in f:
                print line.split('\n')[0]
        return False
    if "-h" in sys.argv:
        with open("help.txt",'r')as f:
            for line in f:
                print line.split('\n')[0]
        return False
    
    if RHOST=="":
        errMsg.append("请在CrawlerConfig.py配置文件下设置爬行目标,或者使用-t参数设置.")
    if int(ThreadNumber)<0:
        errMsg.append("线程并发数不能小于0")
    if int(MaxPic)<0:
        errMsg.append("最大图片爬行量不能小于0")
    if len(errMsg)==0:
        try:
            if os.path.isdir(FILEPATH):
            
    #             print "FILEPATH = "+FILEPATH
                flag = raw_input("文件目录已经存在,是否覆盖该文件目录? (Y/N)")
                if flag=="Y":
                    shutil.rmtree(FILEPATH)
                    os.mkdir(FILEPATH)
                    return True
                else:
                    errMsg.append("请重新指定文件目录" )
                    return False
            else:
                os.mkdir(FILEPATH)
                return True
        except Exception ,e:
            errMsg.append("目录创建失败!请重新试!")
            print e
            return False
    else:
        return False
#     if RHOST
def ErrorPlay():
    for meg in errMsg:
        print meg
    #创建目录
#     File = os.mkdir(FILEPATH)
    
# print FILEPATH
if __name__ == '__main__':
    Building(sys.argv)
#     CheckAuthority()
    if ParamAnalysis():
        print "可以爬行了!"
        wc = ImageCraw(RHOST,ThreadNumber,FILEPATH,MaxPic,TYPE,InnerThread)
        wc.Craw()
    else:
        ErrorPlay()
#         print "设置失败,不能爬行!"
