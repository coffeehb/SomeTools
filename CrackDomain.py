#encoding=utf-8

'''
查找子域名，主要看字典！
'''
import socket

# 导入域名字典1
# 导入域名字典2
DomainDicOne = "E:\domain\domain.txt"
# DomainDicOne = "E:\domain\d.txt"
DomainDicTwo = "E:\domain\domain2.txt"


DomainListOne = []
DomainListTwo = [] 

class CloudFlare:
#         初始化加载字典
        def __init__(self):
                     
            print '''
                            +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                            + thx                       :Barrett                      +
                            + 2014-6-24  modify By      :cf_hb                        +
                            + My Blog                   :coffee.ostrich.cc             +
                            + tips  :                                                 +
                            +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                  '''
            try:
                with open(DomainDicOne,'r')as f:
                    for line in f:
                        DomainListOne.append(line.split('\n')[0])
                
                with open(DomainDicTwo,'r')as f:
                    for line in f:
                        DomainListTwo.append(line.split('\n')[0])
            except Exception,e:
                print "加载字典失败 : ",e
                exit(-1)   # 字典初始化失败，结束程序
                
        def findsubdomain(self,fatherdomain):
            
           for deneyici in DomainListOne:
                try:
                    submain = deneyici +"."+ fatherdomain
                    ip_al = socket.gethostbyname(submain)
                    print "[#] " + deneyici+"."+ fatherdomain +  ", " + ip_al + " --找到子域名...\n"
                except Exception, e:
                    print "[#] 查询记录: ",submain," ---失败"
                    continue
           for deneyici in DomainDicTwo:
                try:
                    submain = deneyici +"."+ fatherdomain
                    ip_al = socket.gethostbyname(submain)
                    print "[#] " + deneyici+"."+ fatherdomain +  ", " + ip_al + " --找到子域名...\n"
                except Exception, e:
                    print "[#] 查询记录:",submain," ---失败"
                    continue
     
# 初始化类，初始化字典集合
x = CloudFlare()

site_url=""
while(site_url ==""):
    site_url = raw_input("[+] Enter Your Site Url (Example : xx.com) : ")

x.findsubdomain(site_url)
