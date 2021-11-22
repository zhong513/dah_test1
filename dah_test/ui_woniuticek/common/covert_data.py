# -*- coding: utf-8 -*-
# 版本       ：1.0
# 功能说明    ：PyCharm
# 作者       ：钟长君
# 创建时间    ：2021/3/22 11:25
# 修改人      ：无
# 修改日期    ：无
def covert(step):  #'影厅名=admin\n影厅类型=123456\n座位选择=0000'
    # data = read_dict_all(sheetname)
    # info = data[0]['step']  # 获取测试步骤的数据 num=10
    if '\n' not in step:  #针对只有一条数据'nub:11'
        li = step.split(':')  # 以冒号分割放在列表
        return li[1]
    else:
        tem=step.strip().split('\n') #['影厅名=admin', '影厅类型=123456', '座位选择=0000']
        da=[]
        for i in tem:
            li=i.split(':') #['影厅名'，'admin']以冒号分割放在列表
            da.append(li[1])
        return da

if __name__ == '__main__':

    if '\n' not in 'moviename:速度':  # 针对只有一条数据
        li = 'moviename:速度'.split(':')  # ['影厅名'，'admin']以冒号分割放在列表
        print(li[1])

