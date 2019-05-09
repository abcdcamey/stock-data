from api.fact.Fact_Market_Ref_Data import Fact_Market_Ref_Data
from api.common.Saver import Saver
from datetime import datetime,timedelta
from api.common.Logs import Logger_process, Logger_process_error

fmrd = Fact_Market_Ref_Data()







def cal_date_func(_date_str):

    Logger_process.log('call Fact_Market_Ref_Daily,' + _date_str)

    Saver.save_to_mysql(fmrd.get_fact_moneyflow_hsgt(_trade_date=_date_str),
                        'fact_moneyflow_hsgt')

    Saver.save_to_mysql(fmrd.get_fact_hsgt_top10(_trade_date=_date_str),
                        'fact_hsgt_top10')

    Saver.save_to_mysql(fmrd.get_fact_ggt_top10(_trade_date=_date_str),
                        'fact_ggt_top10')

    Saver.save_to_mysql(fmrd.get_fact_margin(_trade_date=_date_str),
                        'fact_margin')




cur_date = datetime.now()+timedelta(days=0)
date_str = "%s%02d%s" % (cur_date.year,cur_date.month,cur_date.day)
cal_date_func(date_str)



