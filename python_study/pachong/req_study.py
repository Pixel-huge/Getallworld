#!/usr/bin/env python 
# coding:utf-8
import requests
from bs4 import BeautifulSoup

def download_content(url):
    resp =requests.get(url)
    html_content = resp.content
    soup = BeautifulSoup(html_content,"html.parser")
    print(soup)

if __name__ == '__main__':
    download_content("https://www.runoob.com/python3/python3-tutorial.html")



