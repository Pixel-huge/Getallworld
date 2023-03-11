#!/usr/bin/env python 
# coding:utf-8
import requests
from bs4 import BeautifulSoup
import parse


    # 第一个模板——介绍基本的爬虫程序结构和流程
    #爬取网页内容并保存在一个文档中


def download_content(url):
    """
    第一个函数，用来下载网页，返回网页内容
    参数 url 代表所要下载的网页网址。
    整体代码和之前类似
    """
    response = requests.get(url).content
    return response


# 第二个函数，将字符串内容保存到文件中
# 第一个参数为所要保存的文件名，第二个参数为要保存的字符串内容的变量
def save_to_file(filename, content):
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(content.decode("utf-8"))

def create_doc_from_filename(filename):
    # 输入参数为要分析的 html 文件名，返回值为对应的 BeautifulSoup 对象
    with open(filename, "r", encoding='utf-8') as f:
        html_content = f.read()
        soup = BeautifulSoup(html_content, "html.parser")
    return soup

def parse(soup):
    post_list = soup.find_all("div", id="leftcolumn")   #分析html文件包含需要爬取内容标签位置 属性
    for post in post_list:
        links = post.find_all("a")                          #进一步找到需要的内容
        for link in links:
            text = link.text.strip()                                 #提取文本内容，去掉空格
            url = "https://www.runoob.com/python3"+link["href"]         #获取href 标签的链接，拼接前缀域名
            print(text+":"+url)

def main():
    # 爬取runoob平台的教程url信息
    url = "https://www.runoob.com/python3/python3-tutorial.html"
    filename = "runoob.html"
    result = download_content(url)
    save_to_file(filename, result)
    soup = create_doc_from_filename(filename)
    parse(soup)

if __name__ == '__main__':
    main()


'''
tips：如果想爬取其他网页的内容 该怎么操作？
    ——替换如下几处即可
1，url 替换为想要下载的网页地址
2，filename 替换为网页保存的文件名
3, 是 BeautifulSoup 函数，我们用它一步步从 html 的结构中解析出我们想要的内容，这里我们实现的是首先找到所有 class 属性是 post-info 的 div 标签，然后将这些标签中的 a 标签的文本部分提取出来。

'''

#使用python语言设计一套第一取网页表格信息的脚本