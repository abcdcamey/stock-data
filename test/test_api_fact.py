from api.fact.Fact_Market_Stock_Data import Fact_Market_Stock_Data
from api.common.Saver import Saver
dda = Fact_Market_Stock_Data()


#data = dda.get_fact_market_stock_daily(_trade_date='20190401')
#Saver.save_to_mysql(data,'fact_market_stock_daily')



#data1 = dda.get_market_stock_daily_fq(_ts_code='600000.SH')
#Saver.save_to_xlsx(data1,_file_name='market_stock_daily_fq.xlsx')

#data2 = dda.get_fact_market_stock_weekly(_trade_date='20190419')

#Saver.save_to_mysql(data2,'fact_market_stock_weekly')

#data3 = dda.get_market_stock_weekly_fq(_ts_code='600000.SH')
#Saver.save_to_xlsx(data3,_file_name='market_stock_weekly_fq.xlsx')

#data4 = dda.get_fact_market_stock_monthly(_trade_date='20190329')
#Saver.save_to_mysql(data4,'fact_market_stock_monthly')

#data5 = dda.get_market_stock_monthly_fq(_ts_code='600000.SH')
#Saver.save_to_xlsx(data5,_file_name='market_stock_monthly_fq.xlsx')

#data6 = dda.get_fact_market_stock_suspend(_suspend_date='20190410')
#Saver.save_to_mysql(data6, 'fact_market_stock_suspend')
#data7 = dda.get_fact_market_stock_suspend(_resume_date ='20190412')
#Saver.save_to_mysql(data7, 'fact_market_stock_suspend')



#data8 = dda.get_fact_market_stock_daily_basic(_trade_date='20190410')
#Saver.save_to_mysql(data8,'fact_market_stock_daily_basic')


data9 = dda.get_fact_adj_factor(_trade_date='20190410')
Saver.save_to_mysql(data9,'fact_adj_factor')
