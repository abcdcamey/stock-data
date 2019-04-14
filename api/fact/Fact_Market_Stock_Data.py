from api.common.TuShare_Api_Connect import TuShare_Api_Connect
import tushare as ts

class Fact_Market_Stock_Data:

    def __init__(self):
        tac = TuShare_Api_Connect()
        self._api_connect = tac.get_api_connect()

    def get_market_stock_daily(self, _ts_code = '', _trade_date='', _start_date='',_end_date=''):
        data = self._api_connect.query('daily', ts_code=_ts_code, trade_date=_trade_date, start_date=_start_date, end_date=_end_date)
        return data

    def get_market_stock_daily_fq(self,_ts_code='',_start_date='',_end_date='',_asset='E',_adj='qfq',_freq='D',_ma=''):
        data = ts.pro_bar(api = self._api_connect, ts_code=_ts_code, adj=_adj, start_date=_start_date, end_date=_end_date, asset=_asset, freq=_freq, ma=_ma)
        return data

    def get_market_stock_weekly(self, _ts_code = '', _trade_date='', _start_date='',_end_date=''):
        '''
        :param _ts_code:
        :param _trade_date:
        :param _start_date:
        :param _end_date:
        :return:
        '''
        data = self._api_connect.query('weekly', ts_code=_ts_code, trade_date=_trade_date, start_date=_start_date, end_date=_end_date)
        return data


    def get_market_stock_weekly_fq(self,_ts_code='',_start_date='',_end_date='',_asset='E',_adj='qfq',_freq='W',_ma=''):
        data = ts.pro_bar(api = self._api_connect, ts_code=_ts_code, adj=_adj, start_date=_start_date, end_date=_end_date, asset=_asset, freq=_freq, ma=_ma)
        return data

    def get_market_stock_monthly(self, _ts_code = '', _trade_date='', _start_date='',_end_date=''):
        '''
        :param _ts_code:
        :param _trade_date:
        :param _start_date:
        :param _end_date:
        :return:
        '''
        data = self._api_connect.query('monthly', ts_code=_ts_code, trade_date=_trade_date, start_date=_start_date, end_date=_end_date)
        return data

    def get_market_stock_monthly_fq(self,_ts_code='',_start_date='',_end_date='',_asset='E',_adj='qfq',_freq='M',_ma=''):
        data = ts.pro_bar(api = self._api_connect, ts_code=_ts_code, adj=_adj, start_date=_start_date, end_date=_end_date, asset=_asset, freq=_freq, ma=_ma)
        return data

















