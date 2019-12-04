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
#正则表达
jandanpic = re.findall('src="(.+?).jpg',jandanHTML)


n = 10   #定义n,递增命名图片名
for jpgurl in jandanpic:
    n = n + 1
    jpgurl = "https:" + jpgurl +".jpg"
    # print(jpgurl)
    urllib.request.urlretrieve(jpgurl,r"C:\Users\Admin\Pictures\Jandan\{}.jpg".format(n))
    print("正在下载第" + str(n) + "张图片")
print(r"下载完成!图片保存在C:\Users\Admin\Pictures\Jandan")
