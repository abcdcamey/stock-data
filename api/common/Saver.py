import os
import approot
from .MysqlDB import mysql_conn,cp
from datetime import datetime
import numpy as np
from .Logs import Logger_process, Logger_process_error
import traceback
import StringIO

class Saver:

    def save_to_xlsx(df_data, _path = os.path.join(approot.get_root(), 'data'), _file_name = 'file'):
        df_data.to_excel(os.path.join(_path, _file_name))

    def save_to_mysql(_df, table_name = ''):

        if _df is None or len(_df)==0:
            Logger_process.log("save to mysql,but data is None")
            print("save to mysql,but data is None")
            return
        try:
            Logger_process.log("save to mysql,table name:%s,length:%s" % (table_name, len(_df)))
            print("save to mysql,table name:%s,length:%s" % (table_name , str(len(_df))))
            curs = mysql_conn.cursor()
            sql = cp.get('sql', 'sql_insert')
            table_columns_list = _df.columns.values.tolist() + ['update_dt']
            table_columns_str = ''
            for i in table_columns_list:
                table_columns_str = table_columns_str + '`' + i + '`,'
            table_columns_str = table_columns_str[:len(table_columns_str) - 1]
            value_list = ''
            for i in range(len(_df)):
                value = '('
                for j in range(len(table_columns_list)-1):
                    v = "" if _df.iloc[i, :].get(table_columns_list[j]) is None else _df.iloc[i, :].get(table_columns_list[j])
                    if type(v)==str:
                        v = v.replace('"',"'")
                        value = value + '"' + v + '",'
                    else:
                        if np.isnan(v):
                            v = 'null'
                        value = value + str(v) + ','
                value = value + '"' + str(datetime.now()) + '")'
                value_list = value_list + value + ','
            value_list = value_list[:len(value_list) - 1]
            sql_replaced = sql % (table_name, table_columns_str,value_list)
            curs.execute(sql_replaced)
            mysql_conn.commit()
        except :
            fp = StringIO.StringIO()
            traceback.print_exc(file=fp)
            message = fp.getvalue()
            Logger_process_error.log(message)
            mysql_conn.rollback()
        finally:
            pass
            #mysql_conn.close()




