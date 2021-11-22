# -*- coding: utf-8 -*-
# 版本       ：1.0
# 功能说明    ：PyCharm
# 作者       ：钟长君
# 创建时间    ：2021/3/22 17:01
# 修改人      ：无
# 修改日期    ：无
from business.update_setmeal import up_meal
from common.covert_data import covert
from common.read_excel import read_dict_all
import pytest
dic=read_dict_all('update')#以字典的形式读取所有的数据

@pytest.mark.parametrize('info',dic)

def test_update(info):
    step=info['step'] #步骤对应的数据
    data=covert(step) #转化为列表，里面放这参数
    print(data)
    up_meal('ff').up(data)
    assert 1==1

if __name__ == '__main__':
    pytest.main(['-s',__file__])