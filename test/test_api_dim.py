from api.dim.Dim_Data_Api import Dim_Data_Api
from api.common.Saver import Saver
dda = Dim_Data_Api()

#data = dda.get_stock_basic_list()
#Saver.save_to_xlsx(data,_file_name='stock_basic.xlsx')
#print(type("1")==str)
#Saver.save_to_mysql(data,'stock_basic_list')
#data1 = dda.get_exchange_trade_cal()
#Saver.save_to_xlsx(data1, _file_name='exchange_trade_cal.xlsx')
#Saver.save_to_mysql(data1,'exchange_trade_cal')

#data2 = dda.get_hs_const_list()
#Saver.save_to_xlsx(data2, _file_name='hs_const_list.xlsx')
#Saver.save_to_mysql(data2,'hs_const_list')

#data3 = dda.get_stock_company_basic_info()
#Saver.save_to_xlsx(data3, _file_name='stock_company_basic_info.xlsx')
#Saver.save_to_mysql(data3, 'stock_company_basic_info')

data4 = dda.get_new_share_list()
#Saver.save_to_xlsx(data4, _file_name='new_share_list.xlsx')
Saver.save_to_mysql(data4, 'new_share_list')

data5 = dda.get_stock_name_change()
#Saver.save_to_xlsx(data5, _file_name='stock_name_change.xlsx')
Saver.save_to_mysql(data5, 'stock_name_change')
