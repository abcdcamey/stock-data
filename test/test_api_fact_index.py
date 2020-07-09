from api.fact.Fact_Market_Index_Data import Fact_Market_Index_Data
from api.common.Saver import Saver
fmid = Fact_Market_Index_Data()


#data = fmid.get_fact_market_index_basic(_market='SSE')
#Saver.save_to_mysql(data,'fact_market_index_basic')

#data = fmid.get_fact_market_index_daily(_ts_code='000001.SH' ,_trade_date='20190510')
#Saver.save_to_mysql(data,'fact_market_index_daily')

#data = fmid.get_fact_market_index_weight(_index_code='000001.SH',_start_date='20190409')
#Saver.save_to_mysql(data,'fact_market_index_weight')

data = fmid.get_fact_market_index_dailybasic(_trade_date='20190510',_ts_code='000001.SH')
Saver.save_to_mysql(data,'fact_market_index_dailybasic')
