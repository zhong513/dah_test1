# -*- coding: utf-8 -*-
# 版本       ：1.0
# 功能说明    ：PyCharm
# 作者       ：钟长君
# 创建时间    ：2021/3/23 11:45
# 修改人      ：无
# 修改日期    ：无
from business.select_movie import Select
from common.covert_data import covert
from common.read_excel import read_dict_all
import pytest
dic=read_dict_all('select')#以字典的形式读取所有的数据

@pytest.mark.parametrize('info',dic)
def test_sele(info):
    data=covert('step')
    Select('ff').sele(data)
    assert info['asse_method'] in Select('ff').asse()

if __name__ == '__main__':
    pytest.main(['-s',__file__])