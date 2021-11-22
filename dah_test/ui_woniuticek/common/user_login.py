# -*- coding: utf-8 -*-
# 版本       ：1.0
# 功能说明    ：PyCharm
# 作者       ：钟长君
# 创建时间    ：2021/3/19 10:11
# 修改人      ：无
# 修改日期    ：无
from selenium import webdriver
from common.get_driver import web_driver
from common.read_config import Docof
con=Docof()
url=con.get_value_from_option('userurl','url')#获取用户端登录地址
class U_login:  #调用需要传入游览器
    def __init__(self,browser):
        self.driver = web_driver.get_driver(browser)
        self.driver.get(url)
        self.driver.implicitly_wait(20)

    def user_login(self):

        self.driver.find_element_by_class_name('login-popup').click()
        self.driver.execute_script('document.getElementById("loginuser").value="小黄"')
        self.driver.execute_script('document.getElementById("loginpwd").value="123456"')
        self.driver.find_element_by_xpath('//form[@id="logform"]/a[@class="theme-btn"]').click()#点击登录

        return self.driver



# if __name__ == '__main__':