#!/usr/bin/env python 
# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    # 这里我们定义了一个名为 BasePage 的类，它包含一个名为 find_element 的方法，用于查找指定的页面元素。
    # 这个方法使用了 Selenium 的显式等待机制，等待元素的出现并返回找到的元素
    def __int__(self,driver):
        self.drvier = driver

    def find_element(self, loctaor, timeout=10):
        return WebDriverWait(self.drvier,timeout).until(
            EC.presence_of_element_located(loctaor)
        )





