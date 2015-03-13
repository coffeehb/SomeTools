#encoding=GBK
'''
Created on 2014年10月12日
爬虫主线程
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
程序运行时变量:
TargetURLS: 欲爬行的URLS
OldURLS: 爬行过的URLS

TargetImgs: 将要下载的图片
OldURLS: 已经下载过的图片
'''

OldURLS = []
TargetURLS = []
TargetImgs =[]
OldImgs =[]

RHOST=""
ThreadNumber=0
FILEPATH=""
MaxPic=0 # 爬行线程用这个判断还用不用继续爬行
PicId=1  # 内置下载线程用这个与MaxId对比判断，还用不用继续下载图片.

TyPE=""
InnerThread=5

class ImageCraw:
    '''
              初始化参数
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
                  爬行函数
    '''
    def Craw(self):
        try:
            global ThreadNumber
            global RHOST
            global TargetURLS
            global InnerThread
            #将目标入口链接加入爬行集合中
            TargetURLS.append(RHOST)
            print TargetURLS
            
#             #启动爬行线程
            for i in range(int(ThreadNumber)):
                print "启动爬行线程:"+str(i)
                t = CrawlerThread()
#                 t.setDaemon(True)
                t.setName("CrawlerID :"+str(i))
                t.start()
                 
            time.sleep(5)
            #内置5个线程下载图片启动图片下载线程
            for k in range(int(InnerThread)):
                print "启动图片下载线程:"+str(k)
                dt = ImageDownThread()
#                 dt.setDaemon(True)
                dt.setName("DownloadThreadId :"+str(k))
                dt.start()
        except Exception ,e:
            print "线程启动错误:"
            print e
#             
#执行爬行的线程类

class CrawlerThread(threading.Thread):
    def run(self):
        while True:
            Imgs = []
            Urls =[]
            #1爬页面
            webContent = self.openUrl()
            #2取数据
            Imgs =self.ExtractImages(webContent)
            Urls = self.ExtractUrls(webContent)
            #3更新数据
            flg = self.UpdateImageURLS(Imgs)
            print "______________flg:",flg
            if flg==False: #图片够了不用爬行了!
                break
            else:
                self.UpdateTargetURLS(Urls)
        print "********爬虫: "+self.getName()+"结束爬行!******"
        
    def openUrl(self):
        webContext=""
        getNextUrl = ""
        while True:
            getNextUrl = self.GetNextURL()
            print "正在爬行的链接:"+getNextUrl
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
#页面里解析新的链接出来
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
#         print "获取下一个爬行链接:"+targetUrl
        return targetUrl
#提取图片
#matc = re.findall('http://[^<][^>]+?.jpg', content)

    def ExtractImages(self,webContent):
#         print"爬取结果中抽出图片"
        imgs = re.findall('http://[^<][^>]+?.jpg',webContent)
#         for  img in imgs:
#             print(img)
#         print "+++++++++++++++++++++++爬到新图片++++++++++++++++++++++++++"
#         for im in imgs:
#             print "+++++++++"+im
        return imgs
    
#提取URLS
# href=".+?"
    def ExtractUrls(self,webContent):
#         print "爬取结果中抽取URLS"
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
#需要处理掉其他站点的链接和 / # 链接 
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
        
#         print "++++++++++++++++++++++爬到新URL+++++++++++++++++"
#         for n in newURL3:
#             print "---------"+n
#得到最终的URL
        return newURL3
#修改爬到的图片表
    def UpdateImageURLS(self,NewImages):
        
        global TargetImgs
        global OldImgs
        global MaxPic
        global PicId
        
        flg=False #True 表示图片不够,False表示图片够了
        try:
            
            while True: #一直等待拿锁
                
                if PicId>=int(MaxPic):
                    flg=False
                    break
                flag = mutex.acquire
                if flag:#拿到锁,更新图片列表.
                    
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
                    else:#图片够了不爬行了
                        flg=False
                        mutex.release()
                        break
                else:    #没有拿到,就继续申请.
                    time.sleep(1)
                    continue
            return flg
        except Exception,e:
            print "......................出现异常............................"
            print e
            return flg
            
#更新爬到的链接
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
执行图片下载的线程类
'''
class ImageDownThread(threading.Thread):
    def run(self):
        ImageLink=""
        fg = True
        while True:
            try:
                ImageLink = self.GetImageUrl()
                fg = self.DownLoad(ImageLink)
                if fg:#返回True 表示图片需要继续下载
                    print ".....下载ing...."
                    continue
                else: #图片已经下载够 了,结束下载了.
                    print ".....下载完成...."
                    break
                
            except Exception , e:
                print e
        print "+++++++++++++++内置下载线程+"+self.getName()+"结束++++++++++++++++"
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
#         print "准备下载的下一个图片: "+ImageUrl
        return ImageUrl
    
#返回结果为True 表示图片没有下载够,False表示图片下载够了
    def DownLoad(self,ImageUrl):
        global imageName
        global FILEPATH
        global PicId
        global MaxPic
        print "*********************最多"+str(MaxPic)+"张图片***************"
        realPath=""
        try:
            #该图片的绝对路径
            while True:
                print "正在下载的图片: "+ImageUrl
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
                    else:#图片下载数量够了
                        print "********************************************************"
                        print "********************************************************"
                        print "*************************图片够了*************************"
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
        #             print "下载完成，开始存放图片.."
                    File = open(realPath,'wb')
                    File.write(img)
                    File.close()
                return True
            
        except Exception,e:
            print "下载失败!"
            print e
            return True #下载失败,下一次重新下载
        
            