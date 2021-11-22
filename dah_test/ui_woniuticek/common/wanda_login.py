# -*- coding: utf-8 -*-
# 版本       ：1.0
# 功能说明    ：PyCharm
# 作者       ：钟长君
# 创建时间    ：2021/3/18 19:55
# 修改人      ：无
# 修改日期    ：无
from common.read_config import Docof
from common.get_driver import web_driver

do=Docof()
#影视端登录的地址
url=do.get_value_from_option('wanda',"url")

class W_login:
    def __init__(self,browser):
        self.driver = web_driver.get_driver(browser)
        self.driver.get(url)
        self.driver.implicitly_wait(20)
    def Wan_login(self):
        self.driver.execute_script('document.getElementById("login-username").value="wanda"')#输入用户名
        self.driver.execute_script('document.getElementById("login-password").value="123456"')#输入密码
        self.driver.find_element_by_id('loginbyaccount').click() #点击登录
        return self.driver



# if __name__ == '__main__':
#    W_login('ff').Wan_login()