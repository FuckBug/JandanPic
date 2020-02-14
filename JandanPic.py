"""
该文件已更新在同一级目录下的文件夹中
这是最初的版本,功能只能下载一页图片
为了更好地体验,建议使用新版本
"""

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
