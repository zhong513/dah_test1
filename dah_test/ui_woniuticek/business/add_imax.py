# -*- coding: utf-8 -*-
# 版本       ：1.0
# 功能说明    ：PyCharm
# 作者       ：钟长君
# 创建时间    ：2021/3/20 10:18
# 修改人      ：无
# 修改日期    ：无
import time

from common.wanda_login import W_login
from common.element_operation import ElementOperation


class Imax:

    def __init__(self):
        self.driv = ElementOperation(W_login('ff').Wan_login()) #全局的driver传入此类的构造方法，登录返回一个driver

    def imax_manage(self,i_name,i_type,x,y):
        self.driv.click('link text','放映厅管理')
        #定位到内层框架,并切换
        self.driv.frame_to('id','changehtml')
        time.sleep(2)
        # 定位到下拉框
        self.driv.select_option('xpath','//select[@class="form-control"]')
        time.sleep(2)

        #点击新增按钮
        self.driv.click('id','closeCard1')
        #点击新增影片
        self.driv.click('id','showAddModel')

        #输入影厅名
        self.driv.input(i_name,'id','roomname')
        #影厅类型
        self.driv.input(i_type,'id','roomtype')
        #座位选择
        self.driv.input(x,'id','x')
        self.driv.input(y,'id','y')
        #点击保存
        time.sleep(1)
        self.driv.click('xpath','//input[@id="kbtn"]')
        #警告框点击确定
        time.sleep(6)
        # self.driv.accept_alert()
        # self.driv.get_pagesource()
# if __name__ == '__main__':
#     Imax().imax_manage('大法师','dsf',2,4)
