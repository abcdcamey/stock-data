import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../"))
from api.fact.Fact_Market_Ref_Data import Fact_Market_Ref_Data
from api.common.Saver import Saver
from datetime import datetime,timedelta
from api.common.Logs import Logger_process, Logger_process_error
import time
from api.dim.Dim_Data_Api import Dim_Data_Api

dda = Dim_Data_Api()
fmrd = Fact_Market_Ref_Data()


def cal_history_func_date(_date_str, i):
    Logger_process.log('call Fact_Market_Ref_History by date,%s,%s' % (_date_str, i))
    print('call Fact_Market_Ref_History by date,%s,%s' % (_date_str, i))
    Saver.save_to_mysql(fmrd.get_fact_moneyflow_hsgt(_trade_date=_date_str),'fact_moneyflow_hsgt')

    Saver.save_to_mysql(fmrd.get_fact_hsgt_top10(_trade_date=_date_str),'fact_hsgt_top10')

    Saver.save_to_mysql(fmrd.get_fact_ggt_top10(_trade_date=_date_str), 'fact_ggt_top10')

    Saver.save_to_mysql(fmrd.get_fact_margin(_trade_date=_date_str), 'fact_margin')

    #Saver.save_to_mysql(fmrd.get_fact_margin_detail(_trade_date=_date_str), 'fact_margin_detail')


    data = fmrd.get_fact_stock_daily_top_list(_trade_date=_date_str)
    Saver.save_to_mysql(data, 'fact_stock_daily_top_list')

    data = fmrd.get_fact_stock_daily_top_inst(_trade_date=_date_str)
    Saver.save_to_mysql(data, 'fact_stock_daily_top_inst')

    data = fmrd.get_fact_stock_repurchase(_ann_date=_date_str)
    Saver.save_to_mysql(data, 'fact_stock_repurchase')

    data = fmrd.get_fact_stock_share_float(_ann_date=_date_str)
    Saver.save_to_mysql(data, table_name='fact_stock_share_float')

    data = fmrd.get_fact_stock_block_trade(_trade_date=_date_str)
    Saver.save_to_mysql(data, table_name='fact_stock_block_trade')

    # 目前只到2019年2月22号的数据
    data = fmrd.get_fact_stock_stk_account(_date =_date_str)
    Saver.save_to_mysql(data, table_name='fact_stock_stk_account')

    time.sleep(5)

def cal_history_func_stock_date(_ts_code,_start_date,_end_date):
    Logger_process.log('call Fact_Market_Ref_History by stock date ,stock:%s,_start_date:%s,_end_date:%s'%(_ts_code,_start_date,_end_date))
    print('call Fact_Market_Ref_History by stock date ,stock:%s,_start_date:%s,_end_date:%s'%(_ts_code,_start_date,_end_date))

    # 每次100条，每支股3年取一次
    data = fmrd.get_fact_top10_holders(_ts_code=_ts_code,_start_date=_start_date,_end_date=_end_date)
    Saver.save_to_mysql(data, 'fact_stock_top10_holders')

    # 每次100条，每支股3年取一次
    data = fmrd.get_fact_top10_floatholders(_ts_code=_ts_code,_start_date=_start_date,_end_date=_end_date)
    Saver.save_to_mysql(data, 'fact_stock_top10_floatholders')
    time.sleep(2)

def cal_history_func_stock(_ts_code):
    Logger_process.log('call Fact_Market_Ref_History by stock,' + _ts_code)
    print('call Fact_Market_Ref_History by stock,' + _ts_code)

    data = fmrd.get_fact_stock_pledge_stat(_ts_code=_ts_code)
    Saver.save_to_mysql(data, 'fact_stock_pledge_stat')

    data = fmrd.get_fact_stock_pledge_detail(_ts_code=_ts_code)
    Saver.save_to_mysql(data, 'fact_stock_pledge_detail')

    data = fmrd.get_fact_stock_concept_detail(_ts_code=_ts_code)
    Saver.save_to_mysql(data, table_name='fact_stock_concept_detail',column_dict= {'id':'concept_code'})

    # 用_ts_code跑历史数据，之后加_ann_date跑每天数据
    data = fmrd.get_fact_stock_stk_holdernumber(_ts_code=_ts_code,)
    Saver.save_to_mysql(data, table_name='fact_stock_stk_holdernumber')
    time.sleep(2)



'''
# 不用跑历史数据，每天更新即可
data = fmrd.get_fact_stock_concept()
Saver.save_to_mysql(data, 'fact_stock_concept', delete_all=True)

for i in range(3099,7000):
    cur_date = datetime.now()+timedelta(days=-i)
    date_str = "%s%02d%02d" % (cur_date.year, cur_date.month, cur_date.day)
    cal_history_func_date(date_str,i)


'''

df_stock_all = dda.get_stock_basic_list()

for i in df_stock_all.index:
    ts_code = df_stock_all.loc[i].get('ts_code')
    print(i,ts_code)
    cal_history_func_stock(ts_code)
    for i in range(0,10000,501):
        end_date = datetime.now() + timedelta(days=-i)
        start_date = datetime.now() + timedelta(days=-(i+500))
        start_date_str = "%s%02d%02d" % (start_date.year, start_date.month, start_date.day)
        end_date_str = "%s%02d%02d" % (end_date.year, end_date.month, end_date.day)

        cal_history_func_stock_date(ts_code,start_date_str,end_date_str)

