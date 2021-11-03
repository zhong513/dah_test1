import paramiko
from dah_test.os_file import mv_pag
def runSshCmd(cmd,*userinof):
    ip=userinof[0]
    name=userinof[1]
    pwd=userinof[2]
    transport = paramiko.Transport(ip, 22)
    # 建立连接
    transport.connect(username=name, password=pwd)
    # 将sshclient的对象的transport指定为以上的transport
    ssh = paramiko.SSHClient()
    ssh._transport = transport
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(cmd)
    # 获取命令结果
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    print(result.decode())
    # 关闭连接
    ssh.close()
    transport.close()

#上传
def putfile(inpath, outpath, *userinof):
    ip=userinof[0]
    name=userinof[1]
    pwd=userinof[2]
    transport = paramiko.Transport(ip, 22)
    # 建立连接
    transport.connect(username=name, password=pwd)
    # 将sshclient的对象的transport指定为以上的transport
    # ssh = paramiko.SSHClient()
    sftp = paramiko.SFTPClient.from_transport(transport)
    # LocalFile.txt 上传至服务器 /home/fishman/test/remote.txt
    sftp.put(inpath, outpath)
    # stdin, stdout, stderr = ssh.exec_command('')
    transport.close()
#下载
def getfile(inpath,outpath,*userinof):
    ip=userinof[0]
    name=userinof[1]
    pwd=userinof[2]
    transport = paramiko.Transport(ip, 22)
    # 建立连接
    transport.connect(username=name, password=pwd)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sftp = paramiko.SFTPClient.from_transport(transport)
    # 将LinuxFile.txt 下载到本地 fromlinux.txt文件中
    sftp.get(outpath,inpath)
    transport.close()

def newcrontab(crontabstr,ip,name,pwd):
    crontabstr="""echo "0 */1 * * * python  /home/kt/getPm/CityDataSpider.py"  >> /opt/zcj/ """
    runSshCmd(crontabstr, ip, name, pwd)
# def linDeploy(ip,name,pwd):
# def putfile(inpath,outpath,*userinof)
#     crontabstr=""
#     runSshCmd(crontabstr,ip.name,pwd)

if __name__ == '__main__':
    local_path=(r"C:\Users\Administrator\Desktop\pag\new\street-app-portal-0.0.1-SNAPSHOT.jar",
           r"C:\Users\Administrator\Desktop\pag\new\dah-street-api-1.0.0-SNAPSHOT.jar",
           r"C:\Users\Administrator\Desktop\pag\new\street.zip")
    linux_path = (r"/opt/zcj/mq/street-app-portal-0.0.1-SNAPSHOT.jar",
                 r"/opt/zcj/mq/dah-street-api-1.0.0-SNAPSHOT.jar",
                 r"/opt/zcj/mq/street.zip")
    for i in range(3):
        putfile(local_path[i], linux_path[i],  "192.167.6.185", "root", "Test123456")
        print(f"{local_path[i]}上传成功...上传至/opt/zcj/mq")
    runSshCmd("sh /opt/zcj/mq/auto_deploy.sh", "192.167.6.185", "root", "Test123456")
    # print("-" * 10 + "保留源版本内容" + "-" * 10)
    # mv_pag()