import pymysql
class Connect_DB:
    def __init__(self,host,user,passwd,db,port=3306,charset='utf8'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
        self.charset = charset
        self.con = None
        self.cur = None
        self.connect()
    def connect(self):
        try:
            self.con = pymysql.connect(user=self.user, password=self.passwd, db=self.db,
                                       port=self.port, charset=self.charset,host=self.host)
        except Exception as e:
            print(e)
            print('连接失败，请检查连接参数')
        else:
            self.cur = self.con.cursor()
    def dml(self,*sql):
        """执行dml操作"""
        try:
            for i in sql:
                self.cur.execute(i)
        except Exception as e:
            print(e)
            print('执行失败，请检查SQL语句')
            self.con.rollback()
        else:
            self.con.commit()

    def get_one(self,sql):
        """获取查询结果中一个数据"""
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_all(self,sql):
        """获取查询结果中的所有数据"""
        self.cur.execute(sql)
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.con.close()
if __name__ == '__main__':
    cd = Connect_DB('192.168.255.184','root','Woniu123','movie')


