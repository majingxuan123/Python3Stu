from typing import Union

from pymysql import Connection


class ConnectMysqlStu:
    # 类属性
    autoCommit = True

    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        # 实例属性
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def selfConnect(self) -> Connection:
        # autocommit=True  代表会自动commit
        conn = Connection(host=self.host, port=self.port, user=self.user, password=self.password,
                          database=self.database, autocommit=ConnectMysqlStu.autoCommit)
        return conn

    @staticmethod
    def staticConnect(host: str, port: int, user: str, password: str, database: str) -> Connection:
        # autocommit=True  代表会自动commit
        conn = Connection(host=host, port=port, user=user, password=password, database=database, autocommit=ConnectMysqlStu.autoCommit)
        return conn

    @classmethod
    def classConnect(cls) -> Connection:
        # cls 只能使用类方法中的元素 无法使用实例方法中的元素
        # autocommit=True  代表会自动commit
        conn = Connection(host=cls.host, port=cls.port, user=cls.user, password=cls.password, database=cls.database, autocommit=ConnectMysqlStu.autoCommit)
        return conn


    @staticmethod
    def query(conn: Connection, sql: str) -> (list[str]):
        outList: list = [Union[str]]
        cursor = conn.cursor()
        cursor.execute(sql)
        res: tuple = cursor.fetchall()
        if res != None:
            for item in res:
                outList.append(str(item))
        cursor.close()
        return outList


if __name__ == '__main__':
    # 这里是用成员方法调用的
    test = ConnectMysqlStu("192.168.88.20", 4000, "root", "Root@123", "game")

    # 这里用类方法调  cls 只能使用类方法中的元素 无法使用实例方法中的元素
    # conn = test.classConnect()
    # 这里用实例方法调
    conn = test.selfConnect()
    print(conn.get_server_info())

    # 这里是用类静态方法调用的
    response = ConnectMysqlStu.query(conn, "select * from t_country")
    for res in response:
        print(res)
