import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../"))
from api.fact.Fact_Market_Stock_Data import Fact_Market_Stock_Data
from api.common.Saver import Saver
from datetime import datetime,timedelta
from api.common.Logs import Logger_process, Logger_process_error

dda = Fact_Market_Stock_Data()


def cal_history_func(_date_str):
    Logger_process.log('call Fact_Market_Stock_History,'+_date_str)
    print('call Fact_Market_Stock_History,'+_date_str)
    Saver.save_to_mysql(dda.get_fact_market_stock_daily(_trade_date=_date_str),
                        'fact_market_stock_daily')

    Saver.save_to_mysql(dda.get_fact_market_stock_weekly(_trade_date=_date_str),
                        'fact_market_stock_weekly')

    Saver.save_to_mysql(dda.get_fact_market_stock_monthly(_trade_date=_date_str),
                        'fact_market_stock_monthly')

    Saver.save_to_mysql(dda.get_fact_market_stock_suspend(_suspend_date=_date_str),
                        'fact_market_stock_suspend')

    Saver.save_to_mysql(dda.get_fact_market_stock_suspend(_resume_date =_date_str),
                        'fact_market_stock_suspend')

    Saver.save_to_mysql(dda.get_fact_market_stock_daily_basic(_trade_date=_date_str),
                        'fact_market_stock_daily_basic')

    Saver.save_to_mysql(dda.get_fact_adj_factor(_trade_date=_date_str),
                        'fact_adj_factor')

for i in range(10):
    cur_date = datetime.now()+timedelta(days=-i)
    date_str = "%s%02d%s" % (cur_date.year, cur_date.month, cur_date.day)
    cal_history_func(date_str)



