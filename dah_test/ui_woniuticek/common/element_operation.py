# -*- coding: UTF-8 -*-
# 项目名:pythonProject
# 功能说明:元素操作
# 文件名:element_operation.py
# 用户名:zcj
# 创建时间:2021/3/19 10:00


# -*- coding: UTF-8 -*-
# 项目名:pythonProject
# 功能说明:未知
# 文件名:test.py
# 用户名:xiamaoyuan
# 创建时间:2021/3/19 10:00

import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import random
class ElementOperation:
    #
    def __init__(self,driver): #传入driver对象，调用次类，先去选择游览器获取唯一driver (get_driver)
        self.driver=driver
    #     '''
    #     创建一个driver供后续操作
    #     :param browser: 浏览器类型
    #     :param url: 地址url
    #     '''
    #     self.driver = None
    #     if browser.lower() in ('chrome', '谷歌'):     # 打开谷歌浏览器
    #         self.driver = webdriver.Chrome()
    #     elif browser.lower() in ('firefox', '火狐','ff'):  # 打开火狐浏览器
    #         self.driver = webdriver.Firefox()
    #     self.driver.maximize_window()  # 最大化浏览器
    #     self.driver.get(url)    # 打开制定页面
    #     self.driver.implicitly_wait(20)  # 全局隐式等待
    def get(self,url):
        self.driver.get(url)

    def imp_wait(self):
        self.driver.implicitly_wait(20)
    def find_element(self,by,value=None):
        """定位一个元素"""
        return self.driver.find_element(by,value)

    def find_elements(self,by,value=None):
        """定位一组元素"""
        return self.driver.find_elements(by,value)

    def input(self,info_data,by,value=None):
        """输入"""
        ele = self.find_element(by,value)
        ele.clear()
        ele.send_keys(info_data)

    def click(self,by,value=None):
        """点击"""
        self.find_element(by,value).click()

    def get_title(self):
        """获取页面标题"""
        return self.driver.title


    def get_pagesource(self):
        """获取页面源码"""
        return self.driver.page_source

    def get_img(self,filename):
        """截图"""
        self.driver.save_screenshot(filename)

    def wait(self,t):
        """等待"""
        time.sleep(t)

    def close(self):
        """关闭当前页面"""
        self.driver.close()

    def execute_js(self,js):
        self.driver.execute_script(js)#执行js

    def get_text(self,by,values):
        ele = self.find_element(by, values)#先定位元素，再获取指定文本
        return  ele.text

    def refresh(self):
        """刷新页面"""
        self.driver.refresh()
    #
    # def __del__(self):
    #     """关闭浏览器"""
    #     self.driver.quit()

    def exec_js(self,js):
        '''执行js代码'''
        self.driver.execute_script(js)

    def alert_text(self):
        return self.driver.switch_to.alert.text
    def accept_alert(self):
        #在警告栏中点击确定
        self.driver.switch_to.alert.accept()
    def dismiss_alert(self):
        #在警告栏中点击取消
        self.driver.switch_to.alert.dismiss()
    def input_alert(self,msg):
        #在警告栏中输入内容
        self.driver.switch_to.alert.send_keys(msg)
    def frame_to(self,*args): #以元组封装传进去  (xpath,value)
        #切换到指定框架
        f=self.find_element(*args)#定位框架 *用来解包  xpath,value
        self.driver.switch_to.frame(f) #切换到框架
    def frame_outter(self):
        #切换到外层框架
        self.driver.switch_to.default_content()
    def select_option(self,*args):
        #随机选择下拉框选项
        s=self.find_element(*args) #定位下拉框
        option=len(Select(s).options)#获取选项数量
        Select(s).select_by_index(random.randint(0,option-1))#随机选择
    #关闭游览器
    def quit(self):
        self.driver.quit()
    #断言等于
    def should_element_equals(self, caseid, by, values, expt):
        # 通过参数how,what得到实际结果>>元素的文本内容
        ele = self.find_element(by, values)
        rest = ele.text
        # 断言
        if expt == rest:
            print(f'<{caseid}> 测试通过!')
        else:
            print(f'<{caseid}> 测试失败!')


# if __name__ == '__main__':
#     r = ElementOperation('火狐','http://192.168.255.184:14200/web/feng/index.html')
#     r.click('link text','登录')
#     r.input("小蓝",'id','loginuser')
#     r.input('123456','id','loginpwd')
#     r.click('xpath',"/html/body/div/div[1]/div[1]/div/form/a")
