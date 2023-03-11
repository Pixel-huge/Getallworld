#!/usr/bin/env python 
# coding:utf-8
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import parse

	#第二个模板——抓取表格，做数据分析

def download_content(url):
	resp = requests.get(url).content
	return resp

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
    table = soup.find_all("table")[1]
    t_rows = table.find_all("tr")
    for row in t_rows:
        country = row.find_all("td")
        for num in country:
            nump = num.text
            print(nump)





def main():
    url = "https://www.boc.cn/sourcedb/whpj/"   #中国银行外汇牌价
    #url = "http://bank.pingan.com/geren/waihuipaijia.shtml"   #平安银行外汇牌价
    filename = "table.html"
    resp_content = download_content(url)
    save_to_file(filename,resp_content)
    soup = create_doc_from_filename(filename)
    parse(soup)

if __name__ == '__main__':
    main()


'''
tips：如果想爬取其他网页的内容 该怎么操作？
    ——替换如下几处即可
1,filename 修改你要保存的 excel 文件名称；
2,url 替换为想要抓取表格所在网页的网址；
3,cmb_table_list[1]  其中【1】替换为表格的序号，比如想要抓取网页中的第几个表格

'''