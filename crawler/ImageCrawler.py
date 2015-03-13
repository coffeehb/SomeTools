#encoding=GBK
'''
Created on 2014��10��12��
�������߳�
@author: cf_hb
'''

import requests as req
import threading
import time
import re
import urllib

from threading import Thread

mutex = threading.Lock()
mutexCraw = threading.Lock()
picMutex = threading.Lock()

'''
��������ʱ����:
TargetURLS: �����е�URLS
OldURLS: ���й���URLS

TargetImgs: ��Ҫ���ص�ͼƬ
OldURLS: �Ѿ����ع���ͼƬ
'''

OldURLS = []
TargetURLS = []
TargetImgs =[]
OldImgs =[]

RHOST=""
ThreadNumber=0
FILEPATH=""
MaxPic=0 # �����߳�������жϻ��ò��ü�������
PicId=1  # ���������߳��������MaxId�Ա��жϣ����ò��ü�������ͼƬ.

TyPE=""
InnerThread=5

class ImageCraw:
    '''
              ��ʼ������
    '''
    def __init__(self,target,number,path,maxPic,typ,InThreaf):
        
        global RHOST
        global ThreadNumber
        global FILEPATH
        global MaxPic
        global InnerThread
        global TyPE
        
        RHOST = target
        ThreadNumber = number
        FILEPATH = path
        MaxPic = maxPic
        TyPE = typ
        InnerThread = InThreaf
        print TyPE
        print InnerThread
        
    '''
                  ���к���
    '''
    def Craw(self):
        try:
            global ThreadNumber
            global RHOST
            global TargetURLS
            global InnerThread
            #��Ŀ��������Ӽ������м�����
            TargetURLS.append(RHOST)
            print TargetURLS
            
#             #���������߳�
            for i in range(int(ThreadNumber)):
                print "���������߳�:"+str(i)
                t = CrawlerThread()
#                 t.setDaemon(True)
                t.setName("CrawlerID :"+str(i))
                t.start()
                 
            time.sleep(5)
            #����5���߳�����ͼƬ����ͼƬ�����߳�
            for k in range(int(InnerThread)):
                print "����ͼƬ�����߳�:"+str(k)
                dt = ImageDownThread()
#                 dt.setDaemon(True)
                dt.setName("DownloadThreadId :"+str(k))
                dt.start()
        except Exception ,e:
            print "�߳���������:"
            print e
#             
#ִ�����е��߳���

class CrawlerThread(threading.Thread):
    def run(self):
        while True:
            Imgs = []
            Urls =[]
            #1��ҳ��
            webContent = self.openUrl()
            #2ȡ����
            Imgs =self.ExtractImages(webContent)
            Urls = self.ExtractUrls(webContent)
            #3��������
            flg = self.UpdateImageURLS(Imgs)
            print "______________flg:",flg
            if flg==False: #ͼƬ���˲���������!
                break
            else:
                self.UpdateTargetURLS(Urls)
        print "********����: "+self.getName()+"��������!******"
        
    def openUrl(self):
        webContext=""
        getNextUrl = ""
        while True:
            getNextUrl = self.GetNextURL()
            print "�������е�����:"+getNextUrl
            try:
                while True:
                    f = urllib.urlopen(getNextUrl)
                    webContext = f.read()
                    
                    if webContext=="":
                        continue
                    else:
                        break
                break
            except Exception,e:
                print e
                break
        return webContext
#ҳ��������µ����ӳ���
    def GetNextURL(self):
        global TargetURLS
        global OldURLS
        targetUrl=""
        while True:
            flg = mutexCraw.acquire() 
            if flg:
                if len(TargetURLS)>0:
                    targetUrl = TargetURLS[0]
                    TargetURLS.remove(targetUrl)
                    OldURLS.append(targetUrl)
                    mutexCraw.release()
                    break
                else:
                    mutexCraw.release()
                    continue
            else:
                time.sleep(2)
                continue
#         print "��ȡ��һ����������:"+targetUrl
        return targetUrl
#��ȡͼƬ
#matc = re.findall('http://[^<][^>]+?.jpg', content)

    def ExtractImages(self,webContent):
#         print"��ȡ����г��ͼƬ"
        imgs = re.findall('http://[^<][^>]+?.jpg',webContent)
#         for  img in imgs:
#             print(img)
#         print "+++++++++++++++++++++++������ͼƬ++++++++++++++++++++++++++"
#         for im in imgs:
#             print "+++++++++"+im
        return imgs
    
#��ȡURLS
# href=".+?"
    def ExtractUrls(self,webContent):
#         print "��ȡ����г�ȡURLS"
        global RHOST
        urls1 = re.findall('href=".+?"',webContent)
        urls2 = re.findall('href=\'.+?\'',webContent)
        newURL=[]
        newURL2=[]
        newURL3=[]
        
        for k in urls1:
            if k in newURL:
                pass
            else:
                newURL.append(k)
        for p in urls2:
            if p in newURL:
                pass
            else:
                newURL.append(p)
#��Ҫ���������վ������Ӻ� / # ���� 
        for m in newURL:
            if m[-6:-1] ==".html":
                newURL2.append(m)
            if m[-2:-1] =="/":
                newURL2.append(m)
        for v in newURL2:
            if "http" in v:
                continue
            elif len(v.split('\''))>2:
                t = v.split('\'')[1]
                t = t.replace("//","/")
                t = RHOST+t
                newURL3.append(t)
            elif len(v.split("\""))>2:
                w = v.split("\"")[1]
                w = w.replace("//","/")
                w = RHOST+w
                newURL3.append(w)
        
#         print "++++++++++++++++++++++������URL+++++++++++++++++"
#         for n in newURL3:
#             print "---------"+n
#�õ����յ�URL
        return newURL3
#�޸�������ͼƬ��
    def UpdateImageURLS(self,NewImages):
        
        global TargetImgs
        global OldImgs
        global MaxPic
        global PicId
        
        flg=False #True ��ʾͼƬ����,False��ʾͼƬ����
        try:
            
            while True: #һֱ�ȴ�����
                
                if PicId>=int(MaxPic):
                    flg=False
                    break
                flag = mutex.acquire
                if flag:#�õ���,����ͼƬ�б�.
                    
                    if int(MaxPic)==0:
                        for img in NewImages:
                            if img[-7:]=="404.jpg":
                                pass
                            elif img in OldImgs:
                                pass
                            elif img in TargetImgs:
                                pass
                            else:
                                TargetImgs.append(img)
                        mutex.release()
                        break
                    elif len(OldImgs)<int(MaxPic):
                        
                        for img in NewImages:
                            
                            if img[-7:]=="404.jpg":
                                pass
                            elif img in OldImgs:
                                pass
                            elif img in TargetImgs:
                                pass
                            else:
                                TargetImgs.append(img)
                        flg = True
                        mutex.release()
                        break
                    else:#ͼƬ���˲�������
                        flg=False
                        mutex.release()
                        break
                else:    #û���õ�,�ͼ�������.
                    time.sleep(1)
                    continue
            return flg
        except Exception,e:
            print "......................�����쳣............................"
            print e
            return flg
            
#��������������
    def UpdateTargetURLS(self,NewUrls):
        try:
            global TargetURLS 
            global OldURLS
            while True:
                flg =  mutexCraw.acquire
                if flg:
                    for nurl in NewUrls:
                        if nurl in OldURLS:
                            pass
                        elif nurl in TargetURLS:
                            pass
                        else:
                            TargetURLS.append(nurl)
                    mutexCraw.release()
                    break
                else:
                    time.sleep(1)
                    continue
        except:
            pass

'''
ִ��ͼƬ���ص��߳���
'''
class ImageDownThread(threading.Thread):
    def run(self):
        ImageLink=""
        fg = True
        while True:
            try:
                ImageLink = self.GetImageUrl()
                fg = self.DownLoad(ImageLink)
                if fg:#����True ��ʾͼƬ��Ҫ��������
                    print ".....����ing...."
                    continue
                else: #ͼƬ�Ѿ����ع� ��,����������.
                    print ".....�������...."
                    break
                
            except Exception , e:
                print e
        print "+++++++++++++++���������߳�+"+self.getName()+"����++++++++++++++++"
    def GetImageUrl(self):
        
        ImageUrl=""
        global TargetImgs 
        global OldImgs
        while True:
            flg =mutex.acquire() 
            if flg:
                if len(TargetImgs)>0:
                    ImageUrl = TargetImgs[0]
                    TargetImgs.remove(ImageUrl)
                    OldImgs.append(ImageUrl)
                    mutex.release()
                    break
                else:
                    mutex.release()
                    continue
            else:
                time.sleep(1)
                continue
#         print "׼�����ص���һ��ͼƬ: "+ImageUrl
        return ImageUrl
    
#���ؽ��ΪTrue ��ʾͼƬû�����ع�,False��ʾͼƬ���ع���
    def DownLoad(self,ImageUrl):
        global imageName
        global FILEPATH
        global PicId
        global MaxPic
        print "*********************���"+str(MaxPic)+"��ͼƬ***************"
        realPath=""
        try:
            #��ͼƬ�ľ���·��
            while True:
                print "�������ص�ͼƬ: "+ImageUrl
                flg = picMutex.acquire()
                
                if flg:
                    
                    if MaxPic==0:
                        realPath = FILEPATH+str(PicId)+".jpg"
                        PicId = PicId + 1
                        picMutex.release()
                        break
                    elif PicId<=int(MaxPic):
#                         print "type(PicId):",type(PicId)
#                         print "type(MaxPic):",type(MaxPic)
                        
#                         print "++++++++++++++PicId:"+str(PicId)+"<="+MaxPic+"++++++++++++++++"
                        realPath = FILEPATH+str(PicId)+".jpg"
                        PicId = PicId + 1
                        picMutex.release()
                        break
                    else:#ͼƬ������������
                        print "********************************************************"
                        print "********************************************************"
                        print "*************************ͼƬ����*************************"
                        print "********************************************************"
                        print "********************************************************"
                        
                        picMutex.release()
                        break
                else:
                    time.sleep(2)
                    continue
            if realPath=="":
                return False
            else:
                web = req.get(ImageUrl)
                if web.status_code ==404:
                    pass
                else:
                    img = web.content
        #             print "������ɣ���ʼ���ͼƬ.."
                    File = open(realPath,'wb')
                    File.write(img)
                    File.close()
                return True
            
        except Exception,e:
            print "����ʧ��!"
            print e
            return True #����ʧ��,��һ����������
        
            