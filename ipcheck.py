#encoding=UTF-8
'''
使用windows自带的ping命令，检测目标IP主机是否存在。
Created on 2014年6月20日
@author: Administrator
'''
# 检查给定IP所在的网段哪些IP在线
import os

def getIps(st):
    if st == "":
        return 0
    else:
        lis = st.split('.')
        ip = lis[0]+"."+lis[1]+"."+lis[2]
    for k in range(1,255):
#         print k
        tp = ip +"."+str(k)
#         print tp
        info=os.popen('ping '+tp).read()
        inf = info.decode("GBK")
#         print(inf)
        if inf.find('TTL') != -1:
            print "存在主机: "+tp
        else:
            continue
ip  =raw_input("请输入目标网段任意IP:")
print "探测开始"
getIps(ip)
print "探测完毕"


