from api.dim.Dim_Data_Api import Dim_Data_Api
from api.common.Saver import Saver
dda = Dim_Data_Api()


Saver.save_to_mysql(dda.get_stock_basic_list(),'stock_basic_list')

Saver.save_to_mysql(dda.get_exchange_trade_cal(),'exchange_trade_cal')

Saver.save_to_mysql(dda.get_hs_const_list(),'hs_const_list')

Saver.save_to_mysql(dda.get_stock_company_basic_info(), 'stock_company_basic_info')

Saver.save_to_mysql(dda.get_new_share_list(), 'new_share_list')

Saver.save_to_mysql(dda.get_stock_name_change(), 'stock_name_change')