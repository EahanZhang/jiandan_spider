#!/bin/bash
#coding=utf-8
import requests
from bs4 import BeautifulSoup

index = 0
headers = {'referer': 'http://jandan.net/', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}

# 保存图片
def save_jpg(res_url):
    global index
    html = BeautifulSoup(requests.get(res_url, headers=headers).text, 'lxml')
    for link in html.find_all('a', {'class': 'view_img_link'}):
        with open('{}.{}'.format(index, link.get('href')[len(link.get('href'))-3 : len(link.get('href'))]), 'wb') as jpg:
            jpg.write(requests.get("http:" + link.get('href')).content)
            print("正在抓取第%s条数据" % index)
            index += 1

if __name__ == '__main__':
    url = 'http://jiandan.net/ooxx'

    while url != '':
        save_jpg(url)
        url = BeautifulSoup(requests.get(url, headers=headers).text, 'lxml').find('a', {'class': 'previous-comment-page'}).get('href')
    else:
        print("爬取完毕")

# res = requests.get('http://jiandan.net/ooxx')
# html = BeautifulSoup(res.text, 'lxml')
# for index, each in enumerate(html.select('.commentlist img')):
#     print str(index) + ": " + each.attrs['src'][2:]
#     # if ".gif" not in each.attrs['src']:
#     #     with open('{}.jpg'.format(index), 'wb') as jpg:
#     #         jpg.write(requests.get("http:" + each.attrs['src'], stream=True).content)
#     with open('{}.jpg'.format(index), 'wb') as jpg:
#         jpg.write(requests.get("http:" + each.attrs['src'], stream=True).content)