import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../"))
from api.fact.Fact_Market_Index_Data import Fact_Market_Index_Data
from api.common.Saver import Saver
from datetime import datetime,timedelta
from api.common.Logs import Logger_process, Logger_process_error
import time
from api.dim.Dim_Data_Api import Dim_Data_Api

fmid = Fact_Market_Index_Data()
market_list=['MSCI', 'CSI', 'SSE', 'SZSE', 'CICC', 'SW']
ts_code_list=['000001.SH', '000016.SH', '399001.SZ', '399005.SZ', '399006.SZ', '399007.SZ']

def cal_history_func_date(_date_str,_ts_code):
    Logger_process.log('call Fact_Market_Index_History by date,'+_date_str)
    print('call Fact_Market_Index_History by date,'+_date_str)


    data = fmid.get_fact_market_index_daily(_ts_code=_ts_code , _trade_date=_date_str)
    Saver.save_to_mysql(data,'fact_market_index_daily')

    #data = fmid.get_fact_market_index_weight(_index_code=_ts_code, _start_date=_date_str)
    #Saver.save_to_mysql(data,'fact_market_index_weight')

    data = fmid.get_fact_market_index_dailybasic(_ts_code=_ts_code, _trade_date=_date_str)
    Saver.save_to_mysql(data, 'fact_market_index_dailybasic')



Saver.save_to_mysql(None, 'fact_market_index_basic',delete_all=True)
for _market in ['MSCI','CSI','SSE','SZSE','CICC','SW']:
    data = fmid.get_fact_market_index_basic(_market=_market)
    Saver.save_to_mysql(data, 'fact_market_index_basic')


for i in range(0,7300):
    cur_date = datetime.now()+timedelta(days=-i)
    date_str = "%s%02d%02d" % (cur_date.year, cur_date.month, cur_date.day)
    for _ts_code in ts_code_list:
        cal_history_func_date(date_str,_ts_code)
    time.sleep(2)