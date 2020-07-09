import os
import approot
from .MysqlDB import MysqlDB,cp
from datetime import datetime
import numpy as np
from .Logs import Logger_process, Logger_process_error
import traceback
from io import StringIO
import time
import pandas as pd
class Query:
    @staticmethod
    def query(column_list = [],table_name = '',condition=dict(),tail_condition = ""):
        try:
            Logger_process.log("query from mysql,column_list:%s,table name:%s,condition:%s" % (column_list,table_name, condition))

            mysql_conn = MysqlDB.get_mysql_conn()
            sql = cp.get('sql', 'sql_query')
            column_str = ",".join(column_list)

            condition_list = []
            for k,v in condition.items():
                if isinstance(v,list):
                    l="','".join(v)
                    condition_list.append("`" + str(k) + "`" + " in ('" + l + "')")
                elif isinstance(v,tuple):
                    condition_list.append("`" + str(k) + "`" + " between '" + v[0] + "' and '"+v[1]+"' " )
                else:
                    condition_list.append("`" + str(k) + "`" + "='" + str(v) + "'")
            condition_str = " and ".join(condition_list)
            if len(condition_str)==0:
                condition_str = "1=1 "
            condition_str = condition_str+tail_condition
            sql_replaced = sql % (column_str, table_name,condition_str)

            Logger_process.log("------sql-------:"+sql_replaced)
            return pd.read_sql(sql_replaced, mysql_conn)

        except :
            mysql_conn = MysqlDB.get_mysql_conn()
            fp = StringIO()
            traceback.print_exc(file=fp)
            message = fp.getvalue()
            Logger_process_error.log(message)
            mysql_conn.rollback()
            raise
        finally:
            pass
            #mysql_conn.close()




