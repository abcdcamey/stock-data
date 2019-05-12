from api.common.Saver import Saver
from api.dim.Dim_Data_Api import Dim_Data_Api
from datetime import datetime, timedelta
from api.common.Logs import Logger_process, Logger_process_error
dda = Dim_Data_Api()


Saver.save_to_mysql(dda.get_stock_basic_list(),'stock_basic_list',delete_all=True)

Saver.save_to_mysql(dda.get_exchange_trade_cal(),'exchange_trade_cal',delete_all=True)

Saver.save_to_mysql(dda.get_hs_const_list(),'hs_const_list',delete_all=True)

Saver.save_to_mysql(dda.get_stock_company_basic_info(), 'stock_company_basic_info',delete_all=True)

Saver.save_to_mysql(dda.get_stock_name_change(), 'stock_name_change',delete_all=True)

# 限制10000条
Saver.save_to_mysql(dda.get_new_share_list(_start_date='19900101',_end_date='20091231'), 'new_share_list',delete_all=True)

Saver.save_to_mysql(dda.get_new_share_list(_start_date='20100101',_end_date='20201231'), 'new_share_list')



'''
Saver.save_to_mysql(None, 'stock_name_change', delete_all=True)

df_stock_all = dda.get_stock_basic_list()
for i in df_stock_all.index:
    ts_code = df_stock_all.loc[i].get('ts_code')

    Saver.save_to_mysql(dda.get_stock_name_change(_ts_code=ts_code), 'stock_name_change')
'''
