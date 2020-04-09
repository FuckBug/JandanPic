# !/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
'Download Meizitu pictures.'
__author__ = 'FuckBug'
https://github.com/FuckBug/JandanPic

I'm a rookie.
If you find some bugs, please correct me.
Thank you for seeing the code.


                                       .::::.
                                     .::::::::.
                                    :::::::::::  FUCK YOU
                                ..:::::::::::'
                              '::::::::::::'
                                .::::::::::
                           '::::::::::::::..
                                ..::::::::::::.
                              ``::::::::::::::::
                               ::::``:::::::::'        .:::.
                              ::::'   ':::::'       .::::::::.
                            .::::'      ::::     .:::::::'::::.
                           .:::'       :::::  .:::::::::' ':::::.
                          .::'        :::::.:::::::::'      ':::::.
                         .::'         ::::::::::::::'         ``::::.
                        ...:::           ::::::::::::'              ``::.
                        ```` ':.          ':::::::::'                  ::::..
                                            '::::::'                    ':'````..


The graphic annotation by: https://blog.csdn.net/wbxaut/article/details/79279909
"""

"""
# 在运行之前,请务必确保您已安装如下模块.
# Make sure you have these modules installed before running.
"""
import requests,re,os
# 获取现有的页数
def getPages(url,headers):
    global page_num     #当前总页数
    request = requests.get(url = url , headers = headers)
    if request.status_code == 200:
        pattern = re.compile('https://www.mzitu.com/zipai/comment-page-(.*?)/#comment', re.S)
        result = re.findall(pattern, request.text)
        page_num = result[0]
        return page_num
    else:
        print("网络异常,请检查您的网络!" + request.status_code)
        return None
n = 0
# 获取本页的图片链接
def getPicLink(pages,headers):
    global picNum, links
    url = "https://www.mzitu.com/zipai/comment-page-" + str(pages) +"/"
    request = requests.get(url = url , headers = headers)
    if request.status_code == 200:
        regex = re.compile('data-.*?al="(.*?)".*?width.*?640',re.S)
        links = re.findall(regex,request.text)

    picNum = str(len(links))
    print("本页链接:"+url+"; 本页抓取到"+ picNum + "张图片\n")
    return links
    print(links)
# 下载图片

def downPic(links):
    global n
    download_path = './Grils/'
    if os.path.exists(download_path) == False:  # 判断文件夹是否已经存在
        os.makedirs(download_path)  # 创建文件夹
    a = 0

    for link in links:

        # 使用图片url中的id作为图片文件名
        regex = re.compile('sinaimg.*?/[a-z0-9]{5,7}/(.+?)\.[a-z]{3}', re.S)
        picName = re.findall(regex, link)
        picName = str(picName[0])
        print("图片名称:{}".format(picName))

        # 先创建一个空文本,以防万一
        with open('./Downloads.txt', 'a') as f:
            f.write('')
        with open('./Downloads.txt', 'r') as f:
            data = f.read()
            data = re.findall(link, data)
        a = a + 1
        if data == []:
            print(pages)
            print("Downloading... 正在下载第{}页第{}张图片 ".format(pages,a))

            # 判断jpg还是gif
            isJpg = re.findall('jpg',link)
            if isJpg:
                downLink = requests.get(link)
                with open(download_path + picName + '.jpg', 'wb')as f:
                    f.write(downLink.content)
                    n = n + 1  # 计数
                    print("OK,本次此次下载{}张,已下载本页第{}张图片,本页还剩{}张待下载\n".format(n, a, (int(picNum) - a)))
            else:
                downLink = requests.get(link)
                with open(download_path + picName + '.gif', 'wb')as f:
                    f.write(downLink.content)
                    n = n + 1  # 计数
                    print("OK,本次此次下载{}张,已下载本页第{}张图片,本页还剩{}张待下载\n".format(n, a, (int(picNum) - a)))
            # 下载记录保存到文本,确保下次不会重复下载
            with open('./Downloads.txt', 'a') as f:
                f.write(link + '\n')
        else:
            print("该图片已经下载过了哦,正在跳过...\n")

# 循环翻页下载
def main():

    url = "https://www.mzitu.com/zipai/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

    # pages = getPages(url,headers)
    global pages
    pages = getPages(url,headers)
    while int(pages) > 0:
        links = getPicLink(pages, headers)
        downPic(links)
        pages = int(pages) - 1
        # print(pages)
    print("\n下载完成!" )
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n已手动停止运行!!!!!")

