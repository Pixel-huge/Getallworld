#!/usr/bin/env python 
# coding:utf-8

import requests
import pandas as pd
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

	#第二个模板——抓取表格，做数据分析

def download_content(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.text
		else:
			return "None"
	except RequestException as e:
		return e


def save_excel(filename):
	html_content = download_content("http://localhost:8000")
	# 调用 read_html 函数，传入网页的内容，并将结果存储在 cmb_table_list 中
	# read_html 函数返回的是一个 DataFrame 的list
	#soup = BeautifulSoup(html_content,"html.parser")
	cmb_table_list = pd.read_html(html_content)
	# 通过打印每个 list 元素，确认我们所需要的是第二个，也就是下标 1
	# print(cmb_table_list)
	cmb_table_list[1].to_excel(filename)


def main():
	filename = "tips2.xlsx"
	save_excel(filename)

if __name__ == '__main__':
	main()


'''
tips：如果想爬取其他网页的内容 该怎么操作？
    ——替换如下几处即可
1,filename 修改你要保存的 excel 文件名称；
2,url 替换为想要抓取表格所在网页的网址；
3,cmb_table_list[1]  其中【1】替换为表格的序号，比如想要抓取网页中的第几个表格

'''