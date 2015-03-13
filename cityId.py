#encoding=utf-8

'''
Created on 2014年7月4日

@author: Administrator
'''
dtid = "CityID.txt"
CList = []
SqlStr = "insert into CITY_CODE ('id','province','cityName','cityCode') values "

with open(dtid,'r')as f2:
    for line in f2:
        CList.append(line.split('\n')[0])
prov = '﻿北京市'
ID = 1
for item in CList:
    if len(item) <8:
        prov = item+'市'
    elif len(item) <10:
        prov = item
    else:
#         print prov,'====>>',item
        index = item.find('=')
        n = index + 1
        cityName = item[n:]
        cityCode = item[0:index]
        st = "("+str(ID)+",'"+prov+"','"+cityName+"','"+cityCode+"'),"
        SqlStr = SqlStr+st
        ID = ID + 1
print 'SQL语句:\n',SqlStr



