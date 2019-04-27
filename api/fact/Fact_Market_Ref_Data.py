from api.common.TuShare_Api_Connect import TuShare_Api_Connect
import tushare as ts
from api.common.Logs import Logger_process, Logger_process_error

class Fact_Market_Ref_Data:

    def __init__(self):
        tac = TuShare_Api_Connect()
        self._api_connect = tac.get_api_connect()

    def get_fact_moneyflow_hsgt(self, _trade_date = '', _start_date = '', _end_date = ''):





