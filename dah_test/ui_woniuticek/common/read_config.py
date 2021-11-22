# -*- coding: UTF-8 -*-
# 项目名:pythonProject
# 文件名:read_config.py
# 用户名:zcj
# 创建时间:2021/3/12 16:24
'''
读取配置文件公用模块
'''



import os
from configparser import ConfigParser

class Docof():
    def __init__(self,file_name='conf.in'):
        file_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +r'\conf\\'+file_name
        self.cp=ConfigParser()
        self.cp.read(file_path,encoding='utf8')

    def get_all_sections(self):
        # 获取所有节点
        return self.cp.sections()
        #获取某个节点里面option对应的值
    def get_value_from_option(self,section,option):
        """

        :param section: 节点名（http）
        :param option:节点下面的选项（url）
        :return:
        """
        return self.cp.get(section,option)

if __name__ == '__main__':
    dc = Docof()
    url = dc.get_value_from_option('server', 'ip')
    print(dc.get_all_sections())
    print(url)
