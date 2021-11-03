# -*- coding: utf-8 -*-
import os
import time

def mv_pag():
    ver = r"C:\Users\Administrator\Desktop\pag\Version"
    page = ["dah-street-api-1.0.0-SNAPSHOT.jar", "street-app-portal-0.0.1-SNAPSHOT.jar", "street.zip"] #开发提供的包
    page_path=r"C:\Users\Administrator\Desktop\pag\new"
    pages = os.listdir(page_path)  #判断此路径下有那些文件，以列表返回
    version = os.listdir(ver) #获取现有的版本号
    d_list = [[x, y] for x in range(2, 5) for y in range(11)] #创建二维列表版本号  int类型 [[2, 0], [2, 1], [2, 2], [2, 3]
    new_dir_path = []     #新创建的目录
    print(f"现有的版本号目录{version}")
    # dir=os.path.join(ver, "0")
    # print(dir)
    if page==pages:   #判断对应的文件是否存在    #``
        print(f"文件全部存在{pages}")  #··
        for i in range(20):
            s = d_list[i]
            list1 = [str(x) for x in s]  # 把列表里面的数字转为字符串
            st = '.'.join(list1)  # 2.0
            versions = "V" + st  # V2.0
            if versions not in version: #不存在对应的版本号，就创建

                dir = os.path.join(ver, f"{versions}")  #拼接路径
                os.system(f"mkdir {dir}")    #创建版本文件夹
                print(f"文件目录{dir}已创建成功")
                new_dir_path.append(dir)
                break
    else:
        print("文件包不全等待中...")
        time.sleep(2)
    for i in pages:
                mv_path = os.path.join(page_path, f"{i}") #移动的路径
                os.system(f"move {mv_path} {new_dir_path[0]} ")
    print(f"对应文件移动至{new_dir_path[0]}" )

if __name__ == '__main__':
    print("-"*10+"保留源版本"+"-"*10)
    mv_pag()