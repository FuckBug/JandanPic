#jandan
#仅用于学习
#页面url = "http://jandan.net/pic/MjAxOTEyMDMtMTE2"
#base64编码   MjAxOTEyMDMtMTE2 = 20191203-116

#需求:下载jandan无聊图
#思路:
#   0:读取jandan首页
#   1:从步骤1 读取页数和页数的url
#   2:读取每页的图片对应的url
#   3:下载并保存
import urllib.request
import re
from bs4 import BeautifulSoup
import time
#读取首页的HTML
url = 'http://jandan.net/pic'
request = urllib.request.urlopen(url)
if request.code == 200:
    print("网络正常")
elif request.code == 404:
    print("404 NOT FOUND")
else:
    print(request.code)
jandanHTML = request.read().decode("utf-8")

#正则表达,提取出原图链接；
# jandanpic = re.findall('<a href="(.+?)large(.+?)" target="_blank" class="view_img_link"',jandanHTML)
jandanpic = re.findall('//wx(.+?)/large(.+?)" target="_blank" class="view_img_link"',jandanHTML)
# jandanpic = re.findall('src="(.+?).jpg',jandanHTML)
# print(jandanpic)


#循环遍历匹配出来的链接
for i in jandanpic:
    #合并链接
    url = "http://wx" + i[0] + "/large" + i[1]
    print(url)

    #定义时间戳为图片命名
    # time = int(time.time() * 1000000)
    NowTime = int(time.time() * 1000000)

    #判断需要保存的图片格式
    PicFormat = re.findall('jpg',url)
    # print(PicFormat)
    if(PicFormat):
        urllib.request.urlretrieve(url, "/Users/callan/pictures/jandan/{}.png".format(NowTime))
    else:
        urllib.request.urlretrieve(url, "/Users/callan/pictures/jandan/{}.gif".format(NowTime))

    print("保存成功,文件名：" + str(NowTime))
