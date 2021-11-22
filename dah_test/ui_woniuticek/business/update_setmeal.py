# -*- coding: utf-8 -*-
# 版本       ：1.0
# 功能说明    ：PyCharm
# 作者       ：钟长君
# 创建时间    ：2021/3/22 15:32
# 修改人      ：无
# 修改日期    ：无
import random
import time

from common.get_driver import web_driver
from common.element_operation import ElementOperation


class up_meal:

    def __init__(self,browser):
        self.driver = web_driver.get_driver(browser)
        self.driver = ElementOperation(self.driver)#全局的driver传入此类的构造方法
        self.driver.get('http://192.168.255.184:14200/web/qian/check-list.html')
        self.driver.imp_wait()

    def up(self,numb):
        self.driver.click('xpath','(//a[@class=""])[1]') #点击套餐管理
        self.driver.click('xpath','(//a[@class=""])[2]')#点击查看套餐
        self.driver.click('xpath','(//button[@class="layui-btn layui-btn-normal hvr-float-shadow"])[1]')#点击修改套餐
        temp=self.driver.find_elements('xpath','//input[@class="menu-input"]') #定位所有的输入域
        inpu=random.choice(temp)  #随机选择一个输入域
        inpu.clear()
        time.sleep(2)
        inpu.send_keys(numb) #输入内容

        self.driver.click('xpath','(//button[@class="sertain-btn layui-btn"])[1]')#点击确定

# if __name__ == '__main__':
#     u=up_meal('ff')
#     u.up(1234)