from api.dim.Dim_Data_Api import Dim_Data_Api
from api.common.Saver import Saver
from datetime import datetime, timedelta

dda = Dim_Data_Api()

def cal_date_func(_start_date_str,_end_date_str):

    Saver.save_to_mysql(dda.get_stock_basic_list(), 'stock_basic_list', delete_all=True)

    Saver.save_to_mysql(dda.get_exchange_trade_cal(),'exchange_trade_cal', delete_all=True)

    Saver.save_to_mysql(dda.get_hs_const_list(), 'hs_const_list', delete_all=True)

    Saver.save_to_mysql(dda.get_stock_company_basic_info(), 'stock_company_basic_info', delete_all=True)

    Saver.save_to_mysql(dda.get_stock_name_change(), 'stock_name_change', delete_all=True)

    # 限制10000条
    Saver.save_to_mysql(dda.get_new_share_list(_start_date=_start_date_str), 'new_share_list')




cur_date = datetime.now()+timedelta(days=0)

date_str = "%s%02d%02d" % (cur_date.year,cur_date.month,cur_date.day)
cal_date_func(date_str,date_str)
