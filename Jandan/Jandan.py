# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# 在运行之前,请务必确保您已安装如下模块.
# Make sure you have these modules installed before running.
import requests, re, os, base64,time



'About'
"""
Download Jandan pictures.
__author__ = 'FuckBug'
This object on github: https://github.com/FuckBug/MyWebSpider/Jandan

I'm a rookie.
If you found some bugs, please correct me fix it's.
Thank you for seeing the code.





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


'抓取网页首页HTML信息'
def web_pages(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    r = requests.get(url=url, headers=headers,timeout = 15)
    if r.status_code != 200:
        print('网络异常!')
        exit()
    html = r.text
    result = re.findall('[e-r]{4}\W{4}[a-z]{6}\W[a-z]{3}\W[a-z]{3}\W[a-zA-Z0-9]+\W+[a-z$]*\W*[a-z]{5}\W{2}[a-z]{8}',
                        html)
    # print(result)
    result = str(result[0]).split('"', 2)
    global page_link
    page_link = 'http:' + result[1]
    # print(page_link)
    global page_num
    # url解码获取当前页数
    page_num = page_link.split('/pic/', 1)
    page_num = page_num[1].split('#', 1)
    page_num = page_num[0]
    page_num = str(base64.b64decode(page_num.encode('utf-8')), 'utf-8')
    page_num = page_num.split('-', 1)
    page_num = page_num[1]
    # print(page_num)
    print("准备抓取第{}页,本页链接:{}".format(page_num, page_link))
    # return page_link


'抓取每页中的图片链接'
def pic_link():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    r = requests.get(url=page_link, headers=headers,timeout = 15)
    if r.status_code != 200:
        print('ERROR,Network status:' + r.status_code)
        exit()
    result = re.findall('[a-z]{2,4}[0-9]{1}\W[a-z]{7}\W[c-n]{2}\W[a-z]{5}\W[a-zA-Z0-9]*\W[f-p]{3}', r.text)
    return result


'下载图片'
def pic_down():
    down_link = pic_link()

    # 检测是否指定下载目录,如果没有则默认在该文件目录下创建JandanPic文件夹
    if not os.path.exists('./JandanPic'):
        os.makedirs('./JandanPic')
        print("下载目录已创建!")

    pic_sum = len(down_link)
    print('本页共抓取到{}张图片链接\n'.format(pic_sum))

    a = 0
    for link in down_link:
        link = 'http://' + link
        print(link)
        a += 1

        # 使用图片url中的id作为图片文件名
        regex = re.compile('.*?/[a-z0-9]{5,6}/(.*?)\W[a-z]{3}', re.S)
        pic_name = re.findall(regex, link)

        pic_name = str(pic_name[0])
        print("图片名称:{}".format(pic_name))


        # 判断图片是否已经下载过
        # 先创建一个空文本,以防万一
        with open('./Downloads.txt', 'a') as f:
            f.write('')
        with open('./Downloads.txt', 'r') as f:
            data = re.findall(link, f.read())

            download_path = './JandanPic'
            if data == []:
                print('OK,Downloading')


                # 判断图片是jpg还是gif格式,并进行下载
                pic_type = re.findall('jpg', link)
                if (pic_type):
                    # urllib.request.urlretrieve(link, download_path + "/{}.jpg".format(pic_name))

                    down = requests.get(link)
                    with open(download_path + "/" + pic_name + ".jpg", 'wb')as f:
                        f.write(down.content)
                    print("OK,已下载本页第{}张图片,本页还剩{}张待下载\n".format(a, (pic_sum - a)))
                else:
                    # urllib.request.urlretrieve(link, download_path + "/{}.gif".format(pic_name))
                    down = requests.get(link)
                    with open(download_path + "/" + pic_name + ".gif" , 'wb')as f:
                        f.write(down.content)
                    print("OK,已下载本页第{}张图片,本页还剩{}张待下载\n".format(a, (pic_sum - a)))

                # 将链接写入到文本中
                with open('./Downloads.txt', 'a') as f:
                    f.write(link + '\n')

            else:
                print('已跳过,因为该图片已经下载过\n')
    print("下载完成!!!本页共下载{}张图片\n\n".format((a)))


'循环下载图片'
def main(num):
    print("开始运行!")
    url = "http://jandan.net/pic"
    a = 1
    while a <= num:
        time.sleep(0.5)
        a += 1
        web_pages(url)

        pic_down()
        time.sleep(0.5)
        url = page_link
    print("任务完成!")


if __name__ == '__main__':
    try:
####################################################################################
                                                                                   #
                                                                                   #
        '请在此输入想要爬取的页面个数,并确保您输入的是大于0的整数'                          #
        num = 100                                                                  #
                                                                                   #
                                                                                   #
####################################################################################
        main(num)
    except KeyboardInterrupt:
        print("\n\n\n已手动停止运行!!!!!!")
