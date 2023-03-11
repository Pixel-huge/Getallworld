import unittest
from selenium import webdriver
from time import sleep


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wd=webdriver.Chrome()
        cls.url='https://www.baidu.com'

    '''def setUp(self):
        print("启动浏览器")
        self.wd=webdriver.Chrome()
        self.url='https://www.baidu.com'
    '''
    @classmethod
    def tearDownClass(cls):
        cls.wd.quit()

    '''def tearDown(self):
        print('关闭浏览器')
        self.wd.quit()
        '''

    #定义一个普通的方法
    def search_keyword(self,keyword):
        self.wd.find_element_by_id('kw').send_keys(keyword)
        self.wd.find_element_by_xpath("//input[@id='su']").click()
        sleep(2)
    #def page_keyword(self,keyword):
        #self.wd.find_element_by_xpath(keyword).text


    def test_baidu_search_selenium(self):
        print('开始输入查询1')
        #查询信息并查看其中一条目信息

        self.wd.get(self.url)
        self.search_keyword('selenium')
        sleep(2)
        self.wd.find_element_by_xpath("//div[@id='2']/h3/a").click()
        sleep(2)
        #page1=self.page_keyword("//div[@id='2']/h3/a")
        page1= self.wd.find_element_by_xpath("//div[@id='2']/h3/a").text
        print(page1)
        i=str('Selenium_百度百科')
        self.assertEqual(i,page1)

    def test_baidu_search_liudehua(self):
        print('开始输入查询')
        # 查询信息并查看其中一条目信息

        self.wd.get(self.url)
        self.search_keyword('刘德华')
        sleep(2)
        self.wd.find_element_by_xpath("//div[@id='1']/h3/a").click()
        sleep(2)
        #page1= self.page_keyword("//div[@id='1']/h3/a")
        page1 = self.wd.find_element_by_xpath("//div[@id='1']/h3/a").text
        print(page1)
        i = str('刘德华_百度百科')
        self.assertEqual(i, page1)






if __name__ == '__main__':
    unittest.main()