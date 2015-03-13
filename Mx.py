#encoding=utf-8
# 刷访问量脚本
# 两种
import urllib2
import urllib
import cookielib
import webbrowser as web

#  查价格： http://p.3.cn/prices/get?skuid=J_1005766&type=1&area=1_72_4137&callback=cnp
while True:
#     打开新窗口的方式
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
        #填充请求头
        opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
        #以post的方法访问登陆页面，访问之后cookieJar会自定保存cookie
        f = opener.open("http://p.3.cn/prices/get?skuid=J_1005766&type=1&area=1_72_4137&callback=cnp")
        data= f.read()
        inf = data.decode("GBK")
        if inf.find("1799.00"):
            print "当前价格: 1799.00"
            continue
        else:
          web.open_new_tab('http://item.jd.com/972747.html',)
        
#         print "data = ",len(data)
#         print data
        
    