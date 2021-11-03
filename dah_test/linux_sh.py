# import paramiko
#
#
# ssh=paramiko.SSHClient()
# #自动添加机器 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# #连接服务器
# ssh.connect(hostname='192.168.168.128', port=22, username='root', password='123456')
# #执行命令：返回3个结果：标准输入、输出、错误
# stdin, stdout, stderr = ssh.exec_command('df')
# #获取输出结果
# # result = stdout.read()
# res, err = stdout.read(), stderr.read()
# result = res if res else err
# print(result.decode())
# # 关闭连接
# ssh.close()

