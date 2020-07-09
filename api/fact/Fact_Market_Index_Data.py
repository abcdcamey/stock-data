from api.common.TuShare_Api_Connect import TuShare_Api_Connect
import tushare as ts
from api.common.Logs import Logger_process, Logger_process_error

class Fact_Market_Index_Data:

    def __init__(self):
        tac = TuShare_Api_Connect()
        self._api_connect = tac.get_api_connect()

    def get_fact_market_index_basic(self, _market='', _publisher='', _category=''):
        data = self._api_connect.query('index_basic', market=_market, publisher=_publisher, category=_category)

        Logger_process.log("call get_fact_market_index_basic api,get data length:%s" % (len(data)))
        print("call get_fact_market_index_basic api,get data length:%s" % (len(data)))

        return data


    def get_fact_market_index_daily(self, _ts_code='', _trade_date='', _start_date='',_end_date=''):
        data = self._api_connect.query('index_daily', ts_code=_ts_code, trade_date=_trade_date, start_date=_start_date,end_date=_end_date)

        Logger_process.log("call get_fact_market_index_daily api,get data length:%s" % (len(data)))
        print("call get_fact_market_index_daily api,get data length:%s" % (len(data)))

        return data

    def get_fact_market_index_weight(self, _index_code='', _trade_date='', _start_date='', _end_date=''):
        data = self._api_connect.query('index_weight', index_code=_index_code, trade_date=_trade_date, start_date=_start_date, end_date=_end_date)

        Logger_process.log("call get_fact_market_index_weight api,get data length:%s" % (len(data)))
        print("call get_fact_market_index_weight api,get data length:%s" % (len(data)))

        return data

    def get_fact_market_index_dailybasic(self, _ts_code='', _trade_date='', _start_date='', _end_date=''):
        data = self._api_connect.query('index_dailybasic', ts_code=_ts_code, trade_date=_trade_date, start_date=_start_date,end_date=_end_date)

        Logger_process.log("call get_fact_market_index_dailybasic api,get data length:%s" % (len(data)))
        print("call get_fact_market_index_dailybasic api,get data length:%s" % (len(data)))

        return data






