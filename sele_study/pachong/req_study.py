#!/usr/bin/env python 
# coding:utf-8
import requests

def download_content(url):
    resp =requests.get(url)
    html_content = resp.text
    print(html_content)

if __name__ == '__main__':
    download_content("https://sms-activate.org/getNumber")



