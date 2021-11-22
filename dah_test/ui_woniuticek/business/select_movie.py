# -*- coding: utf-8 -*-
# 版本       ：1.0
# 功能说明    ：PyCharm
# 作者       ：钟长君
# 创建时间    ：2021/3/23 10:50
# 修改人      ：无
# 修改日期    ：无
#
import time

from common.get_driver import web_driver
from common.element_operation import ElementOperation

class Select:

    def __init__(self,browser):
        self.driver = web_driver.get_driver(browser) #获取全局的driver
        self.driver=ElementOperation(self.driver) #全局的driver传入此类的构造方法
        self.driver.get('http://192.168.255.184:14200/web/feng/index.html')
        self.driver.imp_wait() #隐式等待20s

    def sele(self,content):
        self.driver.click('name','fmovie') #点击输入框
        self.driver.input(content,'name','fmovie') #输入内容
        self.driver.click('xpath','//button[@style="line-height: 50%"]') #点击搜索
        time.sleep(3)

    def asse(self):
        self.res=self.driver.get_text('xpath','//div[@class="transformers-content"]/h2')
        return self.res
if __name__ == '__main__':
    s=Select('ff')
    s.sele('你好')
    print('你好' in s.asse())