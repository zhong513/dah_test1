# -*- coding: utf-8 -*-
# 版本       ：1.0
# 功能说明    ：PyCharm
# 作者       ：钟长君
# 创建时间    ：2021/3/19 11:22
# 修改人      ：无
# 修改日期    ：无
from common.element_operation import *
from common.user_login import *
class Buy_tick:
    #正常购买流程流程
    def tree(self):
        u=ElementOperation(U_login('ff').user_login())#登录返回一个driver对象，元素接受继续使用
        time.sleep(2)
        u.click('link text','电影')#点击电影
        u.click('xpath','(//a[@class="hvr-shutter-out-horizontal"])[3]')#点击电影终结者
        u.click('xpath','(//li[@class="mtype-active"])[1]')
        time.sleep(3)
        u.click('xpath','(//a[@class="ticket"])[1]')#点击购票
        u.click('xpath','(//a[@class="btn-purchase"])[1]')#点击选座购票
        u.click('xpath','(//span[@class="seat selectable"])[22]')#点击选择座位
        u.click('xpath','(//span[@class="seat selectable"])[23]')#点击选择旁边座位
        u.click('xpath','(//span[@class="seat selectable"])[24]')#点击选择旁边座位
        u.click('class name','confirm-btn')#点击选择旁边座位
        u.click('class name','pay-btn')#点击立即支付
        time.sleep(3)
        # u.input('lbnbwg5447@sandbox.com','id','J_tLoginId') #输入支付宝账户
        # u.input('111111','class name','ui-input i-text') #输入支付密码
        # u.click('xpath','//a[@id="J_newBtn"]/span')#点击下一步

if __name__ == '__main__':
    b=Buy_tick()
    b.tree()