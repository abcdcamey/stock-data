from api.fact.Fact_Market_Stock_Data import Fact_Market_Stock_Data
from api.common.Saver import Saver
dda = Fact_Market_Stock_Data()

#data = dda.get_market_stock_daily(_ts_code='600000.SH')
#Saver.save_to_xlsx(data,_file_name='market_stock_daily.xlsx')

#data1 = dda.get_market_stock_daily_fq(_ts_code='600000.SH')
#Saver.save_to_xlsx(data1,_file_name='market_stock_daily_fq.xlsx')

#data2 = dda.get_market_stock_weekly(_ts_code='600000.SH')
#Saver.save_to_xlsx(data2,_file_name='market_stock_weekly.xlsx')

#data3 = dda.get_market_stock_weekly_fq(_ts_code='600000.SH')
#Saver.save_to_xlsx(data3,_file_name='market_stock_weekly_fq.xlsx')


data4 = dda.get_market_stock_monthly(_ts_code='600000.SH')
Saver.save_to_xlsx(data4,_file_name='market_stock_monthly.xlsx')

data5 = dda.get_market_stock_monthly_fq(_ts_code='600000.SH')
Saver.save_to_xlsx(data5,_file_name='market_stock_monthly_fq.xlsx')