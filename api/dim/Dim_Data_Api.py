from api.common.TuShare_Api_Connect import TuShare_Api_Connect

class Dim_Data_Api:

    def __init__(self):
        tac = TuShare_Api_Connect()
        self._api_connect = tac.get_api_connect()

    def get_stock_basic_list(self, _is_hs = '', _list_status='L', _exchange='',
                             _fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs'):
        '''
        :param _is_hs:
        :param _list_status:
        :param _exchange:
        :param _fields:
        :return:
        '''
        data = self._api_connect.query('stock_basic', is_hs=_is_hs, list_status=_list_status, exchange=_exchange, fields=_fields)
        return data

    def get_exchange_trade_cal(self, _exchange='', _start_date='',_end_date='', _is_open=None,
                               _fields='exchange,cal_date,is_open,pretrade_date'):
        '''
        :param _exchange:
        :param _start_date:
        :param _end_date:
        :param _is_open:
        :param _fields:
        :return:
        '''
        data = self._api_connect.query('trade_cal', exchange = _exchange, start_date=_start_date, end_date=_end_date, is_open=_is_open,
                                       fields=_fields)
        return data

    def get_hs_const_list(self, _hs_type='SH', _is_new='',
                               _fields='ts_code,hs_type,in_date,out_date,is_new'):
        '''
        :param _hs_type:
        :param _is_new:
        :param _fields:
        :return:
        '''
        data = self._api_connect.query('hs_const', hs_type = _hs_type, is_new=_is_new,
                                       fields=_fields)
        return data

    def get_stock_name_change(self,_ts_code = '',_start_date = '',_end_date = '',
                              _fields='ts_code,name,start_date,end_date,ann_date,change_reason'):
        '''
        :param _ts_code:
        :param _start_date:
        :param _end_date:
        :param _fields:
        :return:
        '''
        data = self._api_connect.query('namechange', ts_code=_ts_code, start_date=_start_date, end_date=_end_date,
                                       fields=_fields)
        return data

    def get_stock_company_basic_info(self, _exchange='',
                                     _fields='ts_code,exchange,chairman,manager,secretary,reg_capital,' \
                                             'setup_date,province,city,introduction,website,email,office,employees,main_business,business_scope'):
        '''
        :param _exchange:
        :param _fields:
        :return:
        '''
        data = self._api_connect.query('stock_company', exchange=_exchange,
                                       fields=_fields)
        return data

    def get_new_share_list(self, _start_date='', _end_date='',
                           _fields='ts_code,sub_code,name,ipo_date,issue_date,amount,market_amount,'\
                                    'price,pe,limit_amount,funds,ballot'):
        '''
        :param _start_date:
        :param _end_date:
        :param _fields:
        :return:
        '''
        data = self._api_connect.query('new_share', start_date=_start_date,end_date=_end_date,
                                       fields=_fields)
        return data














