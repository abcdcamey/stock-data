from api.fact.Fact_Market_Ref_Data import Fact_Market_Ref_Data
from api.common.Saver import Saver
fmrd = Fact_Market_Ref_Data()


#data = fmrd.get_fact_moneyflow_hsgt(_trade_date='20190508')
#Saver.save_to_mysql(data,'fact_moneyflow_hsgt')


#data = fmrd.get_fact_hsgt_top10(_trade_date='20190508')
#Saver.save_to_mysql(data,'fact_hsgt_top10')


#data = fmrd.get_fact_ggt_top10(_trade_date='20190508')
#Saver.save_to_mysql(data, 'fact_ggt_top10')


#data = fmrd.get_fact_margin(_trade_date='20190508')
#Saver.save_to_mysql(data, 'fact_margin')


#data = fmrd.get_fact_margin_detail(_trade_date='20190508')
#Saver.save_to_mysql(data, 'fact_margin_detail')


# 每次100条，每支股3年取一次
#data = fmrd.get_fact_top10_holders(_ts_code='000002.SZ',_start_date='20000101',_end_date='20041231')
#Saver.save_to_mysql(data, 'fact_stock_top10_holders')

# 每次100条，每支股3年取一次
#data = fmrd.get_fact_top10_floatholders(_ts_code='000002.SZ',_start_date='20000101',_end_date='20041231')
#Saver.save_to_mysql(data, 'fact_stock_top10_floatholders')



#data = fmrd.get_fact_stock_daily_top_list(_trade_date='20190508')
#Saver.save_to_mysql(data, 'fact_stock_daily_top_list')


#data = fmrd.get_fact_stock_daily_top_inst(_trade_date='20190508')
#Saver.save_to_mysql(data, 'fact_stock_daily_top_inst')

#data = fmrd.get_fact_stock_pledge_stat(_ts_code='000002.SZ')
#Saver.save_to_mysql(data, 'fact_stock_pledge_stat')

# 遍历股票
#data = fmrd.get_fact_stock_pledge_detail(_ts_code='000002.SZ')
#Saver.save_to_mysql(data, 'fact_stock_pledge_detail')


#data = fmrd.get_fact_stock_repurchase(_ann_date='20190508')
#Saver.save_to_mysql(data, 'fact_stock_repurchase')

#不用跑历史数据，每天更新即可
#data = fmrd.get_fact_stock_concept()
#Saver.save_to_mysql(data, 'fact_stock_concept')


#data = fmrd.get_fact_stock_concept_detail(_ts_code='600848.SH')
#Saver.save_to_mysql(data, table_name='fact_stock_concept_detail',column_dict= {'id':'concept_code'})


#data = fmrd.get_fact_stock_share_float(_ann_date='20190508')
#Saver.save_to_mysql(data, table_name='fact_stock_share_float')

#data = fmrd.get_fact_stock_block_trade(_trade_date='20190510')
#Saver.save_to_mysql(data, table_name='fact_stock_block_trade')



# 目前只到2019年2月22号的数据
data = fmrd.get_fact_stock_stk_account(_date='20190222')
Saver.save_to_mysql(data, table_name='fact_stock_stk_account')



#用_ts_code跑历史数据，之后加_ann_date跑每天数据
#data = fmrd.get_fact_stock_stk_holdernumber(_ts_code='600848.SH',)
#Saver.save_to_mysql(data, table_name='fact_stock_stk_holdernumber')
