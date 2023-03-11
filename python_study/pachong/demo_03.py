#!/usr/bin/env python 
# coding:utf-8
import urllib3
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

    #第三个模板——批量从网页下载图片

# 第一个函数，用来下载网页，返回网页内容
# 参数 url 代表所要下载的网页网址。
# 整体代码和之前类似
def download_content(url):
	http = urllib3.PoolManager()
	response = http.request("GET", url)
	response_data = response.data
	html_content = response_data.decode()
	return html_content
# 第二个函数，将字符串内容保存到文件中
# 第一个参数为所要保存的文件名，第二个参数为要保存的字符串内容的变量

def save_to_file(filename, content):
	fo = open(filename, "w", encoding="utf-8")
	fo.write(content)
	fo.close()


# 输入参数为要分析的 html 文件名，返回值为对应的 BeautifulSoup 对象
def create_doc_from_filename(filename):
	fo = open(filename, "r", encoding='utf-8')
	html_content = fo.read()
	fo.close()
	doc = BeautifulSoup(html_content, "lxml")
	return doc

def parse_html(doc):
	images = doc.find_all("img")
	for i in images:
		src = i["src"]
		filename = src.split("/")[-1]
		# print(i["src"])
		urlretrieve(src, "tips_3/" + filename)

def main():
	filename = "tips3.html"
	url = "https://www.duitang.com/search/?kw=AI悦创&type=feed"
	result = download_content(url)
	save_to_file(filename, result)
	doc = create_doc_from_filename(filename)
	parse_html(doc)

if __name__ == '__main__':
	main()



'''
tips：如果想爬取其他网页的内容 该怎么操作？
    ——替换如下几处即可
1,filename 修改你要保存的 文件名（网页文件）；
2,url 替换为想要下载网页的网址；
3, tips_3/ 替换为想要保存图片的文件夹，需要创建好文件夹

'''