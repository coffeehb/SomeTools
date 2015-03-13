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
        ##                        С��������ѯ̨                                                                                                     ##
        ##              �ɲ�����=>  1.  PMֵ                                                                                                             ##
        ##                        2. ������ʾ                                                                                                         ##
        ##                        3. �����ʾ                                                                                                         ##
        ##                        4. ������ǿ��                                                                                                     ##
        ##                        5. ����ָ��                                                                                                         ##
        ##                        6. δ����������Ԥ��                                                                                          ##
        ##===========================================================================##
        ##==================������Դ: �ٶ�����API����=====================================##
        ##=======�ٶ�ak�����ַ��http://lbsyun.baidu.com/apiconsole/key=================##
        ##===========================================================================##
    '''

def GetWeather(city):
    try:
        LEVL = {'0':'��','1':'��','2':'�е�','3':'�е�','4':'������','5':'������','6':'�ж���'}
        
        URL = 'http://api.map.baidu.com/telematics/v3/weather?location='+city+'&output=json&ak=xYnaK22d56Fl6rONI31ByzSw'
        reslut = urllib2.urlopen(URL).read() 
        reslut = reslut.decode('UTF-8')
        jsonObject = json.loads(reslut)['results']
        #��ҳ
        Index = jsonObject[0]['index']
        #��������-������ ���� �� δ�����������Ԥ��
        WeatherData = jsonObject[0]['weather_data']
     
        city = jsonObject[0]['currentCity']
        pm = jsonObject[0]['pm25']
        print "    **************************************************************************"
        print "    **"+u'��ѯ����: '+city
        print "    **"+u'��ѯʱ��: '+WeatherData[0]['date']
        print "    **"+u'��������: '+WeatherData[0]['weather']
        print "    **"+u'���շ���: '+WeatherData[0]['wind']
        lev = int(pm) / 50
        print "    **"+u'�������� ָ��  PMֵ: '+pm , LEVL[str(lev)]
        print '''\
    **+PMֵ�ο���Χ:
    **+    0-50        ��
    **+    50-100      ��
    **+    100-200    �е�
    **+    200-300   ������
    **+    300-500   �ж���
    '''
        print "    **"+u"����״��: "+Index[0]['zs']
        print "    **"+u"������ʾ: "
        print "    **  "+Index[0]['des']
        print "    **"+u"����˶���ʾ: "+Index[3]['zs']
        print "    **  "+Index[3]['des']
        print "    **"+u"������ǿ��: "+Index[4]['zs']
        print "    **  "+Index[4]['des']
        print "    **"+u"������ǿ��: "+Index[4]['zs']
        print "    **  "+Index[2]['des']
        print "    **"+u"����ָ��: ��ð-"+Index[2]['zs']
        print "    **  "+Index[2]['des']
        print "    **************************************************************************"
        print "    ****************************δ����������Ԥ��**********************************"
        print "    **************************************************************************"
        print "    **"+u'����: '+WeatherData[1]['date']+"  "+WeatherData[1]['temperature'] 
        print "    **"+u'��������: '+WeatherData[1]['weather']
        print "    **"+u'�������: '+WeatherData[1]['wind']
        print "    **************************************************************************"
        print "    **"+u'����: '+WeatherData[2]['date']+"  "+WeatherData[2]['temperature']
        print "    **"+u'��������: '+WeatherData[2]['weather']
        print "    **"+u'�������: '+WeatherData[2]['wind']
        print "    **************************************************************************"
        print "    **"+u'�����: '+WeatherData[3]['date']+"  "+WeatherData[3]['temperature']
        print "    **"+u'���������: '+WeatherData[3]['weather']
        print "    **"+u'��������: '+WeatherData[3]['wind']
        print "    **************************************************************************"
        return "FOUND"
    except :
        return "NOTFOUND"
if __name__ == "__main__":
    os.popen('chcp 65501')
#     ��ʼ���ű�
    _init_()
    flag = True
    while flag:
        try:
            
            YourCity = raw_input('������Ҫ��ѯ�ĳ�����(����:exit�˳�����):')
            if YourCity =="exit":
                print "       =========================================================================="
                print "       =========================��ӭ�ٴ�ʹ�ñ�����==================================="
                print "       =========================================================================="
                flag = False
                exit(0)
            while YourCity =="" or  YourCity ==None:
                YourCity = raw_input('�Բ�����������Ҫ��ѯ�ĳ�����(����:exit�˳�����):')
                if YourCity =="exit":
                    print "       =========================================================================="
                    print "       =========================��ӭ�ٴ�ʹ�ñ�����==================================="
                    print "       =========================================================================="
                    flag = False
                    exit(0)
    #       ���봦��
            print "��Ҫ��ѯ�ĳ�����:"+YourCity
            UrlEncodeCity = urllib.quote(YourCity.decode(sys.stdin.encoding).encode('utf8'))
            res = GetWeather(UrlEncodeCity)
            
            if res =="NOTFOUND":
                print u"���ѯ�ĳ���δ֪����ȷ�Ϻ����²�ѯ��"
        except Exception ,e:
            flag = False
            print "Sorry��������쳣���볢��������������"
        
    
    




