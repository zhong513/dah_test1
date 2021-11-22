# -*- coding: utf-8 -*-
# 版本       ：1.0
# 功能说明    ：PyCharm
# 作者       ：钟长君
# 创建时间    ：2021/3/23 10:03
# 修改人      ：无
# 修改日期    ：无
from business.delete_setmeal import delete_meal
import pytest
l=[[1],[2]]

@pytest.mark.parametrize('info',l)

def test_del(info):
    d=delete_meal('ff')
    d.dele()
    assert d.asse()==1

if __name__ == '__main__':
    pytest.main(['-s',__file__])