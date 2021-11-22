# -*- coding: UTF-8 -*-
# 项目名:pythonProject
# 文件名:read_excel.py
# 用户名:zcj
# 创建时间:2021/3/12 16:25
import os
import xlrd
read_exc_path=os.path.dirname(__file__)#当前文件的目录在系统的绝对路径
path=os.path.dirname(read_exc_path)#项目路径
data_path=os.path.join(path,'data')#测试数据的路径
case_path=os.path.join(path,'case')

def read_one(sheetname,x,y):#用名字指定sheet页面，哪一行，哪一列，的单独数据
    try:
        data=xlrd.open_workbook(data_path+'/GUIcase.xlsx')#文件名
        sheet=data.sheet_by_name(sheetname)
        tab=sheet.row_values(x)[y] #index下标获取
        return tab
    except Exception as e:
        print(e)
def read_all(sheetname):# 读取全部内容以列表套列表返回，一行一个小列表
    try: #异常处理
        data = xlrd.open_workbook(data_path+'/GUIcase.xlsx')
        sheet = data.sheet_by_name(sheetname)
        nrow = sheet.nrows#行数从1开始
        info = []  #[['用例名称', '搜索影片', '', '', ''], ['接口URL', 'http://192.168.255.184:14200/api-comment/comment?', '', '', ''],
        for i in range(nrow):
            info.append(sheet.row_values(i))
        return info
    except Exception as e:
        print(e)

def read_dict_all(sheetname):
    try:
        data=xlrd.open_workbook(data_path+'/GUIcase.xlsx')
        sheet=data.sheet_by_name(sheetname) #用名字指定sheet页
        nrow=sheet.nrows #行数从1开始
        info=[]  #最后的数据为[{'case_name': 'login_case_001', 'describe': '用户输入正确的用户名、密码、\n验证码登录成功', 'test_type': 'GUI',
        for row in range(1,nrow): #对知道行数的execl表做字典处理
            dict={}
            dict['case_name']=sheet.cell(row,0).value#从1开始取1，0的数据 （2行第1列的数据）
            dict['describe']=sheet.cell(row,1).value
            dict['test_type']=sheet.cell(row,2).value
            dict['module']=sheet.cell(row,3).value
            dict['class']=sheet.cell(row,4).value
            dict['method']=sheet.cell(row,5).value
            dict['step']=sheet.cell(row,6).value
            dict['asse_method']=sheet.cell(row,7).value
            dict['expect']=sheet.cell(row,8).value
            info.append(dict)
        return info
    except Exception as e:
        print(e)

#-------------------

if __name__ == '__main__':
    print(read_dict_all('select'))


















# class Xlrd:
#     def __init__(self, case_file_name):
#         # 打开 path路径的  excel文件
#         self.excel = xlrd.open_workbook('./Case/'+case_file_name)
#
#     def get_sheet(self, sheet_name=None, sheet_index=None):
#         '''
#         根据excel文件、sheet页名称或者下标返回sheet对象！
#         :param sheet_name:  str
#         :param sheet_index:  str
#         :return:
#         '''
#         # sheet = ''
#         if sheet_name:
#             sheet = self.excel.sheet_by_name(sheet_name)
#         elif sheet_index:
#             sheet = self.excel.sheet_by_index(int(sheet_index))
#         else:
#             sheet = ''
#             print('您的参数输入有误，请确认！')
#         return sheet


# if __name__ == '__main__':
#     r = Xlrd('woniuticket.xlsx')
#     sheets = r.get_sheet(sheet_name='Sheet1')
#     data = sheets.row_values(1)
#     for i in range(10):
#         data = sheets.row_values(i+1)
#         print(data)