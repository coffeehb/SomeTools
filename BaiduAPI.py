#encoding=GBK

import urllib2
import urllib
import json
import sys
import os

def _init_():
    print '''
        ##===========================================================================##
        ##===========================================================================##
        ##                        小龙天气查询台                                                                                                     ##
        ##              可查数据=>  1.  PM值                                                                                                             ##
        ##                        2. 穿衣提示                                                                                                         ##
        ##                        3. 外出提示                                                                                                         ##
        ##                        4. 紫外线强度                                                                                                     ##
        ##                        5. 健康指数                                                                                                         ##
        ##                        6. 未来三天天气预报                                                                                          ##
        ##===========================================================================##
        ##==================数据来源: 百度天气API数据=====================================##
        ##=======百度ak申请地址：http://lbsyun.baidu.com/apiconsole/key=================##
        ##===========================================================================##
    '''

def GetWeather(city):
    try:
        LEVL = {'0':'优','1':'良','2':'中等','3':'中等','4':'不健康','5':'不健康','6':'有毒害'}
        
        URL = 'http://api.map.baidu.com/telematics/v3/weather?location='+city+'&output=json&ak=xYnaK22d56Fl6rONI31ByzSw'
        reslut = urllib2.urlopen(URL).read() 
        reslut = reslut.decode('UTF-8')
        jsonObject = json.loads(reslut)['results']
        #首页
        Index = jsonObject[0]['index']
        #天气数据-包括： 今天 和 未来三天的天气预测
        WeatherData = jsonObject[0]['weather_data']
     
        city = jsonObject[0]['currentCity']
        pm = jsonObject[0]['pm25']
        print "    **************************************************************************"
        print "    **"+u'查询城市: '+city
        print "    **"+u'查询时间: '+WeatherData[0]['date']
        print "    **"+u'今日天气: '+WeatherData[0]['weather']
        print "    **"+u'今日风向: '+WeatherData[0]['wind']
        lev = int(pm) / 50
        print "    **"+u'空气质量 指数  PM值: '+pm , LEVL[str(lev)]
        print '''\
    **+PM值参考范围:
    **+    0-50        优
    **+    50-100      良
    **+    100-200    中等
    **+    200-300   不健康
    **+    300-500   有毒害
    '''
        print "    **"+u"气候状况: "+Index[0]['zs']
        print "    **"+u"穿衣提示: "
        print "    **  "+Index[0]['des']
        print "    **"+u"外出运动提示: "+Index[3]['zs']
        print "    **  "+Index[3]['des']
        print "    **"+u"紫外线强度: "+Index[4]['zs']
        print "    **  "+Index[4]['des']
        print "    **"+u"紫外线强度: "+Index[4]['zs']
        print "    **  "+Index[2]['des']
        print "    **"+u"健康指数: 感冒-"+Index[2]['zs']
        print "    **  "+Index[2]['des']
        print "    **************************************************************************"
        print "    ****************************未来三天天气预报**********************************"
        print "    **************************************************************************"
        print "    **"+u'明天: '+WeatherData[1]['date']+"  "+WeatherData[1]['temperature'] 
        print "    **"+u'明天天气: '+WeatherData[1]['weather']
        print "    **"+u'明天风向: '+WeatherData[1]['wind']
        print "    **************************************************************************"
        print "    **"+u'后天: '+WeatherData[2]['date']+"  "+WeatherData[2]['temperature']
        print "    **"+u'后天天气: '+WeatherData[2]['weather']
        print "    **"+u'后天风向: '+WeatherData[2]['wind']
        print "    **************************************************************************"
        print "    **"+u'大后天: '+WeatherData[3]['date']+"  "+WeatherData[3]['temperature']
        print "    **"+u'大后天天气: '+WeatherData[3]['weather']
        print "    **"+u'大后天风向: '+WeatherData[3]['wind']
        print "    **************************************************************************"
        return "FOUND"
    except :
        return "NOTFOUND"
if __name__ == "__main__":
    os.popen('chcp 65501')
#     初始化脚本
    _init_()
    flag = True
    while flag:
        try:
            
            YourCity = raw_input('请输入要查询的城市名(输入:exit退出程序):')
            if YourCity =="exit":
                print "       =========================================================================="
                print "       =========================欢迎再次使用本程序==================================="
                print "       =========================================================================="
                flag = False
                exit(0)
            while YourCity =="" or  YourCity ==None:
                YourCity = raw_input('对不起，请您输入要查询的城市名(输入:exit退出程序):')
                if YourCity =="exit":
                    print "       =========================================================================="
                    print "       =========================欢迎再次使用本程序==================================="
                    print "       =========================================================================="
                    flag = False
                    exit(0)
    #       编码处理
            print "你要查询的城市是:"+YourCity
            UrlEncodeCity = urllib.quote(YourCity.decode(sys.stdin.encoding).encode('utf8'))
            res = GetWeather(UrlEncodeCity)
            
            if res =="NOTFOUND":
                print u"你查询的城市未知，请确认后重新查询。"
        except Exception ,e:
            flag = False
            print "Sorry程序出现异常，请尝试重新启动程序。"
        
    
    




