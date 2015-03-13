#encoding=GBK
'''
Created on 2014��10��12��
�������߳�
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
#����Ĭ�ϵ�ͼƬ·��
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
#           print "�����߳�����"
            ThreadNumber = argvs[p+1]
            p = p + 1
            continue
        if "-l"==argvs[p]:
#                 print "�������ͼƬ��������"
            MaxPic = argvs[p+1]
            p = p + 1
            continue
        if "-o"==argvs[p]:
#                 print "����·��"
            FILEPATH = argvs[p+1]
            p = p + 1
            continue
        if "-t"==argvs[p]:
#                 print "��������Ŀ��"
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
        errMsg.append("����CrawlerConfig.py�����ļ�����������Ŀ��,����ʹ��-t��������.")
    if int(ThreadNumber)<0:
        errMsg.append("�̲߳���������С��0")
    if int(MaxPic)<0:
        errMsg.append("���ͼƬ����������С��0")
    if len(errMsg)==0:
        try:
            if os.path.isdir(FILEPATH):
            
    #             print "FILEPATH = "+FILEPATH
                flag = raw_input("�ļ�Ŀ¼�Ѿ�����,�Ƿ񸲸Ǹ��ļ�Ŀ¼? (Y/N)")
                if flag=="Y":
                    shutil.rmtree(FILEPATH)
                    os.mkdir(FILEPATH)
                    return True
                else:
                    errMsg.append("������ָ���ļ�Ŀ¼" )
                    return False
            else:
                os.mkdir(FILEPATH)
                return True
        except Exception ,e:
            errMsg.append("Ŀ¼����ʧ��!��������!")
            print e
            return False
    else:
        return False
#     if RHOST
def ErrorPlay():
    for meg in errMsg:
        print meg
    #����Ŀ¼
#     File = os.mkdir(FILEPATH)
    
# print FILEPATH
if __name__ == '__main__':
    Building(sys.argv)
#     CheckAuthority()
    if ParamAnalysis():
        print "����������!"
        wc = ImageCraw(RHOST,ThreadNumber,FILEPATH,MaxPic,TYPE,InnerThread)
        wc.Craw()
    else:
        ErrorPlay()
#         print "����ʧ��,��������!"
