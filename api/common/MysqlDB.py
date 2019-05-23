import pymysql
import configparser
import approot
import os

cp = configparser.ConfigParser()
cp.read(os.path.join(approot.get_root(),'api/config/database.conf'))
db_host = cp.get('db', 'db_host')
db_user = cp.get('db', 'db_user')
db_pwd = cp.get('db', 'db_pwd')
db_name = cp.get('db', 'db_name')
mysql_conn = pymysql.connect(host=db_host, port=3306, user=db_user, passwd=db_pwd, db=db_name, use_unicode=True,
                           charset="utf8")
class MysqlDB:

    @staticmethod
    def get_mysql_conn():
        return mysql_conn












