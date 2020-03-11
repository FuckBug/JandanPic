# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'Download Jandan pictures.'
__author__ = 'FuckBug'

"""
I'm a rookie.
If you find a bug, please correct me.
Thank you for seeing the code.
https://github.com/FuckBug/JandanPic




                                                    ##
                                                    ####
                                               ##############
                                            ####################
                                         ##########################
                                       ##############################
                                       ##############################
                                     ##########  ###########  #########
                                     ##################################
                                  ##################    ##################
                               #####################    #####################
                            ####################################################
                            ####################################################
                            ####################################################
                            ####################################################
                                  ########################################
                                     ##################################
                                     ##################################
                                        ############################
                                            ####################
                                              @@  @@@@@@@@  @@
                                                ||        ||
                                               ++++      ++++

                                              摸鱼使我快乐@Jandan





"""
# 在运行之前,请务必确保您已安装如下模块.
# Make sure you have these modules installed before running.
import urllib.request
import requests,re,os,base64


# ________________________________________________________________________
#  Config                                                                |
url = "http://jandan.net/pic"     # 无需修改                              |
download_path = r''               # 默认下载到该文件目录下Jandan文件夹(选填) |
num = 3                           # 下载的页数,默认下载3页(选填)            |
# _______________________________________________________________________|


'抓取网页首页HTML信息'
def web_pages(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    r = requests.get(url=url, headers=headers)
    if r.status_code != 200:
        print('网络异常!')
        exit()
    html = r.text
    result = re.findall('[e-r]{4}\W{4}[a-z]{6}\W[a-z]{3}\W[a-z]{3}\W[a-zA-Z0-9]+\W+[a-z$]*\W*[a-z]{5}\W{2}[a-z]{8}',html)
    # print(result)
    result = str(result[0]).split('"',2)
    global page_link
    page_link = 'http:' + result[1]
    # print(page_link)

    # url解码获取当前页数
    page_num = page_link.split('/pic/',1)
    page_num = page_num[1].split('#',1)
    page_num = page_num[0]
    page_num = str(base64.b64decode(page_num.encode('utf-8')),'utf-8')
    page_num = page_num.split('-',1)
    page_num = page_num[1]
    # print(page_num)
    print("准备抓取第{}页,本页链接:{}".format(page_num,page_link))
    # return page_link


'抓取每页中的图片链接'
def pic_link():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    r = requests.get(url = page_link, headers = headers)
    if r.status_code != 200:
        print('ERROR,Network status:'+ r.status_code)
        exit()
    result = re.findall('[a-z]{2,4}[0-9]{1}\W[a-z]{7}\W[c-n]{2}\W[a-z]{5}\W[a-zA-Z0-9]*\W[f-p]{3}',r.text)
    return result

'下载图片'
def pic_down(download_path):
    down_link = pic_link()

    # 检测是否指定下载目录,如果没有则默认在该文件目录下创建JandanPic文件夹
    if download_path == '':
        download_path = './JandanPic'
        if not os.path.exists(download_path):
            os.makedirs(download_path)
    pic_sum = len(down_link)
    print('本页共抓取到{}张图片链接\n'.format(pic_sum))

    a = 0
    for link in down_link:
        link = 'http://' + link
        # print(link)
        a += 1
        # 使用图片url中的id作为图片文件名
        pic_name = link.split('/large/',1)
        pic_name = pic_name[1].split('.',1)
        pic_name = pic_name[0]
        print("图片名称:{}".format(pic_name))

        # 判断图片是否已经下载过
        # 先创建一个空文本,以防万一
        with open('./Downloads.txt', 'a') as f:
            f.write('')
        with open('./Downloads.txt', 'r') as f:
            data = f.read()
            data = re.findall(link, data)
                
            if data == []:
                print('OK,Downloading')

                # 判断图片是jpg还是gif格式,并进行下载
                pic_type = re.findall('jpg', link)
                if (pic_type):
                    #防止网络异常导致报错
                    def auto_down():
                        try:
                            urllib.request.urlretrieve(link,download_path + "/{}.jpg".format(pic_name))
                            print("OK,已下载本页第{}张图片,本页还剩{}张待下载\n".format(a,(pic_sum-a)))
                        except urllib.error.ContentTooShortError:
                            print('网络异常,正在尝试重新下载!')
                            auto_down()
                else:
                    urllib.request.urlretrieve(link,download_path + "/{}.gif".format(pic_name))
                    print("OK,已下载本页第{}张图片,本页还剩{}张待下载\n".format(a,(pic_sum-a)))
                    def auto_down():
                        try:
                            urllib.request.urlretrieve(link, download_path + "/{}.gif".format(pic_name))
                            print("OK,已下载本页第{}张图片,本页还剩{}张待下载\n".format(a, (pic_sum - a)))
                        except urllib.error.ContentTooShortError:
                            print('网络异常,正在尝试重新下载!')
                            auto_down()
                # 将链接写入到文本中
                with open(down_history ,'a') as f:
                    f.write(link + '\n')

            else:
                print('已跳过,因为该图片已经下载过\n')
    print("下载完成!!!本页共下载{}张图片\n\n".format((a)))

'循环下载图片'
def down_all(num):
    url = "http://jandan.net/pic"
    a = 1
    while a <= num:
        a += 1
        web_pages(url)
        pic_down(download_path)
        url = page_link
    print("任务完成!")


    try:
        down_all(num)
    except KeyboardInterrupt:
        print("\n已手动停止运行!!!!!")

