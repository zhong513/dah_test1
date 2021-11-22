# -*- coding: utf-8 -*-
# 版本       ：1.0
# 功能说明    ：PyCharm
# 作者       ：钟长君
# 创建时间    ：2021/3/22 20:15
# 修改人      ：无
# 修改日期    ：无
from common.con_db import Connect_DB
from common.element_operation import ElementOperation
from common.get_driver import web_driver

# db=Connect_DB('192.168.255.184','root','Woniu123','movie')
# #数据预埋，新增套餐
# db.dml('INSERT INTO `movie`.`menu` (`id`, `name`, `money`, `period`, `mpic`) VALUES (11, "ee套餐", 500, 3, NULL);')
# db.dml('INSERT INTO `movie`.`menu` (`id`, `name`, `money`, `period`, `mpic`) VALUES (13, "ee套餐", 500, 3, NULL);')
# db.dml('INSERT INTO `movie`.`menu` (`id`, `name`, `money`, `period`, `mpic`) VALUES (14, "ee套餐", 500, 3, NULL);')

class delete_meal:

    def __init__(self,browser):
        self.driver = web_driver.get_driver(browser)
        self.driver = ElementOperation(self.driver)#全局的driver传入此类的构造方法
        self.driver.get('http://192.168.255.184:14200/web/qian/check-list.html')
        self.driver.imp_wait()

    def dele(self):
        self.driver.click('xpath','(//a[@class=""])[1]') #点击套餐管理
        self.driver.click('xpath','(//a[@class=""])[2]')#点击查看套餐
        self.driver.click('xpath', '(//button[@class="layui-btn layui-btn-normal hvr-float-shadow"])[3]')  # 点击修改套餐
        self.star=len(self.driver.find_elements('xpath','//button[@class="layui-btn-radius layui-btn hvr-curl-top-left"]'))
        self.driver.click('xpath','(//button[@class="layui-btn-radius layui-btn hvr-curl-top-left"])[1]') #删除第一个套餐
        self.driver.click('xpath','(//button[@class="sertain-btn layui-btn"])[3]')#点击确定
        self.driver.accept_alert()
        self.end=len(self.driver.find_elements('xpath','//button[@class="layui-btn-radius layui-btn hvr-curl-top-left"]'))
    def asse(self):
         return self.star-self.end #删除成功就为1


