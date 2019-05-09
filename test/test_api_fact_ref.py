from api.fact.Fact_Market_Ref_Data import Fact_Market_Ref_Data
from api.common.Saver import Saver
fmrd = Fact_Market_Ref_Data()


#data = fmrd.get_fact_moneyflow_hsgt(_trade_date='20190429')
#Saver.save_to_mysql(data,'fact_moneyflow_hsgt')


#data = fmrd.get_fact_hsgt_top10(_trade_date='20190429')
#Saver.save_to_mysql(data,'fact_hsgt_top10')


#data = fmrd.get_fact_ggt_top10(_trade_date='20190411')
#Saver.save_to_mysql(data, 'fact_ggt_top10')


#data = fmrd.get_fact_margin(_trade_date='20190411')
#Saver.save_to_mysql(data, 'fact_margin')

#data = fmrd.get_fact_margin_detail(_trade_date='20190411')
#Saver.save_to_mysql(data, 'fact_margin_detail')


#data = fmrd.get_fact_top10_holders(_ts_code='000002.SZ')
#Saver.save_to_mysql(data, 'fact_stock_top10_holders')

data = fmrd.get_fact_top10_floatholders(_ts_code='000002.SZ')
Saver.save_to_mysql(data, 'fact_stock_top10_floatholders')