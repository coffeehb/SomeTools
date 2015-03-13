说明: 图片爬虫，可以爬行 类似http://www.22mm.cc/  静态图片网站

思路与设计: 

思路：
分为了两部分：

第一部分： 爬虫爬行线程类：CrawlerThread
第二部分：内置图片下载线程：ImageDownThread
全局变量解释：

TargetURLS:目标URL
OldURLS: 爬行过的URL
TargetImgs:目标图片
OldImgs:下载过的图片
PicId:下载过的图片计数变量

爬虫线程：

1. 爬虫等待并从TargetURLS中读取下一个爬行URL，读取返回内容。
2. 分析页面，读取URLs 和图片
3. 爬虫线程查看PicId 判断图片是否足够：
   yes: 退出更新TargetImgs，中止爬虫线程
   no: 更新TargetImgs，更新：TargetURLS
4. 重复上述1、2、3



内置图片下载线程：

1. 等待并从TargetImgs中读取图片链接
2. 读取到后更新TargetImgs、OldImgs
3. 下载线程读取:PicId,判断图片是否足够
   yes: 退出下载，结束线程。
   no: 获得绝对路径及图片文件名，并下载图片
4. 重复1、2、3


开发环境： Eclipse + Pydev +Win8（x64）  Python2.7
项目编码：GBK
开发版本：v1.0

开发时间：2014-10-12----2014-10-16


总结：爬虫肯定有很多不足之处，真是尽力写了，不过试了可以用的.

哪些可以改进的地方：
1. 爬虫应当可以识别爬行目标的服务器类型，然后调整自己爬行策略（URL正则筛选）。
2. 爬虫应当能够识别：http://www.22mm.cc/mm/qingliang/PiaePdeCibbaimbme.html 之外的其他URL表示形式
3. 多线程之间数据共享上可以更加优化，比如下载线程 一次读取两个图片URl下载 或三个可能比读取一个然后等线程切换的时间花销更少。
