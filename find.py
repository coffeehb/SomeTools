#encoding=utf-8
import urllib2
import urllib
import cookielib
#先登陆页面
login_page = "http://kcxt.cdu.edu.cn/eol/homepage/common/login.jsp"

LogTxt = "E:\user.txt"
#定义一个登陆检查函数
def renrenBrower():
    
    try:
        #cookieJar作为参数，获得一个opener的实例
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
        #填充请求头
        opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
        #登陆信息
        data = urllib.urlencode({"IPT_LOGINUSERNAME":"201110421212","IPT_LOGINPASSWORD":"lc1991hou"})
        #以post的方法访问登陆页面，访问之后cookieJar会自定保存cookie
        f = opener.open(login_page,data)
#         data= f.read()
#         inf = data.decode("GBK")
#         print "data = ",inf
        #以带cookie的方式访问页面
        val = 50000
#         
#         Url = "http://kcxt.cdu.edu.cn/eol/popups/viewstudent_info.jsp?SID=50000&from=welcomepage";
#         print Url 
#         op=opener.open(Url)
#         #读取页面源码
#         data= op.read()
#         inf = data.decode("GBK")
#         print inf
#         
#         name = unicode("杨雪雯","GBK")
        for val in range(27097,30000):
            
            Url = "http://kcxt.cdu.edu.cn/eol/popups/viewstudent_info.jsp?SID="+str(val)+"&from=welcomepage";
            op=opener.open(Url)
            #读取页面源码
            data= op.read()
            inf = data.decode("GBK")
#             print inf[930:1300]
#             print inf[1144:3500]
            if len(inf) >1000:
                p = inf.find("infotable_bw_vt")
                end = inf.find("button")
                msg = inf[p-46:end-30]
                print msg
            else:
                continue
#             logTxt = open(LogTxt,"a+")
#             logTxt.write(msg+"\n")
#             logTxt.close()
            
#             print inf 
#             uninf = unicode(inf,"GBK")
#             if(uninf.find(name) ==-1):
#                 continue
#             else:
#                 print "*******找到了*********"
#                 print inf
             
    except Exception,e:
        print e
         
renrenBrower()
    