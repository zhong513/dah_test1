# -*- coding: UTF-8 -*-
# 项目名:pythonProject
# 功能说明:未知
# 文件名:test_run.py
# 用户名:xiamaoyuan
# 创建时间:2021/3/19 9:56
import pytest,allure,os,allure_pytest
from common.read_excel import case_path
if __name__ == '__main__':
    pytest.main([f'--alluredir=./rep/tem',case_path])
    os.system('allure generate ./rep/tem -o ./report --clean')
    os.system('allure open -h 127.0.0.1 -p 8883 ./report/')