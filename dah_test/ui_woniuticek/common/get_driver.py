# -*- coding: utf-8 -*-
# 版本       ：1.0
# 功能说明    ：PyCharm
# 作者       ：钟长君
# 创建时间    ：2021/3/19 11:47
# 修改人      ：无
# 修改日期    ：无
from selenium import webdriver
class web_driver:
    driver=None #将driver定义为类级变量，则该driver变量只会保存在类的内存,方便全局只使用一个driver
    @classmethod #直接类名调用，不需要实列化(方法本身不会随着实列化而实列化)
    def get_driver(cls,browser): #指定游览器，返回driver对象
        try:
            if cls.driver is None:
                if browser.lower() in ('chrome', '谷歌'):  # 打开谷歌浏览器
                    cls.driver = webdriver.Chrome() #本地电脑设置了环境变量
                elif browser.lower() in ('firefox', '火狐','ff'):  # 打开火狐浏览器
                    cls.driver = webdriver.Firefox()
            return cls.driver
        except Exception as e:
            print(e)
