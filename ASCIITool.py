#encoding=GBK
'''
Created on 2014��9��2��
@author: cf_hb
'''
import sys
print '''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                        ASCII-Tool                     +
+                   Created on 2014��9��2��             +
+                   @author: CF_HB                      +
+-------------------------------------------------------+
+ASCIIToCHAR:  python ASCIITool.py aTc + �ַ���         +
+(����ַ����ö��ŷֿ������ַ����ڿո��ö����滻)       +
+-------------------------------------------------------+
+example:
+----python ASCIITool.py cTa  hello,hanmeimei-----------+   
+result:
+104,101,108,108,111,44,104,97,110,109,101,105,109,101,105+
+-------------------------------------------------------+
+CHARToASCII:   python ASCIITool.py   cTa     +data     +
+-------------------------------------------------------+
+example:
+ python ASCIITool.py cTa 104,101,108,108,111,44,104,97,110,109,101,105,109,101,105
+result:h e l l o , h a n m e i m e i-------------------+
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      '''
def ASCIIToCHAR(ascStr):
    try:
        lis = ascStr.split(',')
        print "�ַ���:",
        for m in lis:
            print ("%c" % int(m)),
    except:
        print "ת���������������:��(����)����"
        
def CHARToASCII(charStr):
    print charStr
    try:
        asStr= ""
        for k in charStr:
            ac = ord(k)
            asStr = asStr+","+str(ac)
        print "ASCII: ",asStr[1:]
        
    except:
        print "ת��ʧ�������������ַ���!"
if __name__ == '__main__':
    length=len(sys.argv)
    if length !=3:
        exit(0)
    if sys.argv[2]!="" and sys.argv[1]!=None:
        if sys.argv[1]=="cTa":
            CHARToASCII(sys.argv[2])
        elif sys.argv[1]=="aTc":
            ASCIIToCHAR(sys.argv[2])
    else:
        print "�������ʾ������ȷ�Ĳ���!"