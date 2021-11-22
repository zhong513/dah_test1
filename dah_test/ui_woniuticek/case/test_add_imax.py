# -*- coding: utf-8 -*-
# 版本       ：1.0
# 功能说明    ：PyCharm
# 作者       ：钟长君
# 创建时间    ：2021/3/22 10:27
# 修改人      ：无
# 修改日期    ：无
from business.add_imax import Imax
from common.covert_data import covert
from common.read_excel import read_dict_all
import pytest
dic=read_dict_all('add')#以字典的形式读取所有的数据


@pytest.mark.parametrize('info',dic)
def test_add(info):
    step=info['step']
    print(step)
    data=covert(step)#转化为列表，里面放这参数
    print(data)
    Imax().imax_manage(data[0],data[1],data[2],data[3])
    assert 1==1


if __name__ == '__main__':
    pytest.main(['-s',__file__])



