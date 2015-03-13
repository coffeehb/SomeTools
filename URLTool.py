#encoding=GBK
import sys
import urllib as Tool

print '''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                        URL-Tool                       +
+                   Created on 2014年8月14日            +
+                   @author: CF_HB                      +
+-------------------------------------------------------+
+        EncodeURL:python URLTool.py E gb2312/GBK +data +
+-------------------------------------------------------+
+------example: python URLTool.py gb2312  中国----------+   
+------result:   %D6%D0%B9%FA---------------------------+
+-------------------------------------------------------+
+         Decode:python URLTool.py   D     +data        +
+-------------------------------------------------------+
+------example: python URLTool.py D %D6%D0%B9%FA
+------result:中国--------------------------------------+
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      '''
def EncodeURL(Etype,data):
    try:
        unData=""
        try:
            unData = data.decode('utf-8')
        except :
            unData = data.decode('GBK')
            
        EData = unData.encode(Etype)
        url = {'name':EData}
        
        print Tool.urlencode(url)
    except:
        print 'Sorry! please try again !!'

def DecodeURL(enData):
    print "data:",enData
    Ddata =""
    try:
        Ddata = Tool.unquote(enData).decode('gb2312')
    except:
        try:
            Ddata = Tool.unquote(enData).decode('GBK')
        except:
            try:
                Ddata = Tool.unquote(enData).decode('UTF-8')
            except:
                print "Error!"
    try:
        result = Ddata.encode('GBK')
        print result
    except:
        try:
            result = Ddata.encode('gb2312')
            print result
        except:
            try:
                result = Ddata.encode('UTF-8')
                print result
            except:
                print 'ERROR!'

if __name__ == '__main__':
    length=len(sys.argv)
    if length==4 and sys.argv[1]=="E":
        EncodeURL(sys.argv[2],sys.argv[3])
    if length==3 and sys.argv[1]=="D":
        DecodeURL(sys.argv[2])
