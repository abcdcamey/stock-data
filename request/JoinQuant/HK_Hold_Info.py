from api.common.JQSDK_Connect import JQSDK_Connect
from api.common.Saver import Saver
from api.common.Query import Query
from request.JoinQuant.Base_Object import Base_Object
from jqdatasdk import *

class HK_Hold_Info(Base_Object):
    def __init__(self):
        self.sql_table_name = "jq_hk_hold_info"

    def save_by_query_date(self,date):
        df_hk_hold_info = finance.run_query(query(finance.STK_HK_HOLD_INFO).filter(finance.STK_HK_HOLD_INFO.day == date))

        df_hk_hold_info = df_hk_hold_info.rename({"day": "date"}, axis=1)
        df_hk_hold_info['date'] = df_hk_hold_info['date'].astype(str)
        Saver.save_to_mysql(df_hk_hold_info,self.sql_table_name)

    def get_hk_hold_info(self, start_date='', end_date=''):
        df_hk_hold_info = self.query_by_condition(condition={"date": (start_date, end_date)})
        return df_hk_hold_info

if __name__=='__main__':
    hk_Hold_Info = HK_Hold_Info()
    #hk_Hold_Info.save_by_query_date('2020-07-02')

    #df = hk_Hold_Info.query_by_condition({"date":"2020-07-02"})
    df = hk_Hold_Info.get_hk_hold_info(start_date='2020-07-01', end_date='2020-07-06')
    print(df)
