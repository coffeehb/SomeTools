#encoding=gbk
'''
Created on 2014��9��26��

@author: Long-Cong
'''
import requests

print '''
      ++++++++++++++++++++++++++++++++++++++++++
      ++++++++++++++++++Ip����++++++++++++++++++
      +++++++++++++++���������Ա�Ip��+++++++++++++++
      +++++++++++++++����quit�뿪����+++++++++++++++
'''

while True:
    try:
        print "����quit�뿪����"
        ip = raw_input("Enter Your IP:")
        if ip=="quit":
            print "byebye"
            break
        r = requests.get("http://ip.taobao.com/service/getIpInfo.php?ip="+ip)
        
        print r.json()['data']['ip']
        print r.json()['data']['country']
        print r.json()['data']['area']
        print r.json()['data']['region']
        print r.json()['data']['city']
        print r.json()['data']['county']
        print r.json()['data']['isp']
    except:
        print "IP is not matched, Please Try Again!"
    