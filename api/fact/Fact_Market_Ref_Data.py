from api.common.TuShare_Api_Connect import TuShare_Api_Connect
import tushare as ts
from api.common.Logs import Logger_process, Logger_process_error

class Fact_Market_Ref_Data:

    def __init__(self):
        tac = TuShare_Api_Connect()
        self._api_connect = tac.get_api_connect()

    def get_fact_moneyflow_hsgt(self, _trade_date='', _start_date='', _end_date=''):
        data = self._api_connect.query('moneyflow_hsgt',trade_date=_trade_date, start_date=_start_date,
                                       end_date=_end_date)
        Logger_process.log("call get_fact_moneyflow_hsgt api,get data length:%s" % (len(data)))
        return data

    def get_fact_hsgt_top10(self, _ts_code = '', _trade_date='', _start_date='', _end_date='', _market_type=''):
        data = self._api_connect.query('hsgt_top10', ts_code=_ts_code, trade_date=_trade_date, start_date=_start_date,
                                       end_date = _end_date, market_type = _market_type)
        Logger_process.log("call get_fact_hsgt_top10 api,get data length:%s" % (len(data)))
        return data

    def get_fact_ggt_top10(self, _ts_code='', _trade_date='', _start_date='', _end_date='', _market_type=''):
        data = self._api_connect.query('ggt_top10', ts_code=_ts_code, trade_date=_trade_date, start_date=_start_date,
                                       end_date=_end_date, market_type=_market_type)
        Logger_process.log("call get_fact_ggt_top10 api,get data length:%s" % (len(data)))
        return data

    def get_fact_margin(self, _trade_date='', _exchange_id=''):
        data = self._api_connect.query('margin', trade_date=_trade_date, exchange_id=_exchange_id)
        Logger_process.log("call get_fact_margin api,get data length:%s" % (len(data)))
        return data

    def get_fact_margin_detail(self, _trade_date='', _ts_code=''):
        data = self._api_connect.query('margin_detail', trade_date=_trade_date, ts_code=_ts_code)
        Logger_process.log("call get_fact_margin_detail api,get data length:%s" % (len(data)))
        return data

    def get_fact_top10_holders(self,_ts_code='',_period='',_ann_date='',_start_date='',_end_date=''):
        data = self._api_connect.query('top10_holders',ts_code=_ts_code, period=_period, ann_date=_ann_date, start_date=_start_date, end_date=_end_date)
        Logger_process.log("call get_fact_top10_holders api,get data length:%s" % (len(data)))
        return data

    def get_fact_top10_floatholders(self,_ts_code='',_period='',_ann_date='',_start_date='',_end_date=''):
        data = self._api_connect.query('top10_floatholders',ts_code=_ts_code, period=_period, ann_date=_ann_date, start_date=_start_date, end_date=_end_date)
        Logger_process.log("call get_fact_top10_floatholders api,get data length:%s" % (len(data)))
        return data

    def get_fact_stock_daily_top_list(self,_ts_code='',_trade_date=''):
        data = self._api_connect.query('top_list', ts_code=_ts_code, trade_date=_trade_date)
        Logger_process.log("call get_fact_stock_daily_top_list api,get data length:%s" % (len(data)))
        return data

    def get_fact_stock_pledge_stat(self,_ts_code=''):
        data = self._api_connect.query('pledge_stat', ts_code=_ts_code)
        Logger_process.log("call get_fact_stock_pledge_stat api,get data length:%s" % (len(data)))
        return data

    def get_fact_stock_pledge_detail(self,_ts_code=''):
        data = self._api_connect.query('pledge_detail', ts_code=_ts_code)
        Logger_process.log("call get_fact_stock_pledge_detail api,get data length:%s" % (len(data)))
        return data

    def get_fact_stock_repurchase(self, _ann_date='',_start_date='',_end_date=''):
        data = self._api_connect.query('repurchase', ann_date=_ann_date,start_date=_start_date,end_date=_end_date)
        Logger_process.log("call get_fact_stock_repurchase api,get data length:%s" % (len(data)))
        return data

    def get_fact_stock_concept(self, _src='ts'):
        data = self._api_connect.query('concept',src=_src)
        Logger_process.log("call get_fact_stock_concept api,get data length:%s" % (len(data)))
        return data

    def get_fact_stock_concept_detail(self, _id='',_ts_code=''):
        data = self._api_connect.query('concept_detail',id=_id,ts_code=_id)
        Logger_process.log("call get_fact_stock_concept_detail api,get data length:%s" % (len(data)))
        return data

    def get_fact_stock_share_float(self,_ts_code='',_period='',_ann_date='',_start_date='',_end_date=''):
        data = self._api_connect.query('share_float',ts_code=_ts_code, period=_period, ann_date=_ann_date, start_date=_start_date, end_date=_end_date)
        Logger_process.log("call get_fact_stock_share_float api,get data length:%s" % (len(data)))
        return data

    def get_fact_stock_block_trade(self,_ts_code='',_trade_date='',_start_date='',_end_date=''):
        data = self._api_connect.query('block_trade',ts_code=_ts_code,trade_date=_trade_date, start_date=_start_date, end_date=_end_date)
        Logger_process.log("call get_fact_stock_block_trade api,get data length:%s" % (len(data)))
        return data

    def get_fact_stock_stk_account(self, _date='', _start_date='', _end_date=''):
        data = self._api_connect.query('stk_account', date=_date, start_date=_start_date, end_date=_end_date)
        Logger_process.log("call get_fact_stock_stk_account api,get data length:%s" % (len(data)))
        return data

    def get_fact_stock_stk_holdernumber(self,_ts_code='',_enddate='',_start_date='',_end_date=''):
        data = self._api_connect.query('stk_holdernumber',ts_code=_ts_code,enddate=_enddate, start_date=_start_date, end_date=_end_date)
        Logger_process.log("call get_fact_stock_stk_holdernumber api,get data length:%s" % (len(data)))
        return data

    def get_fact_stock_stk_holdertrade(self,_ts_code='',_ann_date='',_start_date='',_end_date='',_trade_type='',_holder_type=''):
        data = self._api_connect.query('stk_holdertrade',ts_code=_ts_code,ann_date=_ann_date, start_date=_start_date, end_date=_end_date, trade_type=_trade_type, holder_type=_holder_type)
        Logger_process.log("call get_fact_stock_stk_holdertrade api,get data length:%s" % (len(data)))
        return data

