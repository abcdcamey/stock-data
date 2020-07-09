from api.common.JQSDK_Connect import JQSDK_Connect
from api.common.Saver import Saver
from api.common.Query import Query
from request.JoinQuant.Base_Object import Base_Object
from jqdatasdk import *

class Global_Idx_Daily(Base_Object):
    def __init__(self):
        self.sql_table_name = "jq_global_idx_daily"

    def save_by_query_date(self,date):
        df_global_idx_daily = finance.run_query(query(finance.GLOBAL_IDX_DAILY).filter(
                                                                 finance.GLOBAL_IDX_DAILY.day==date).limit(5000))
        df_global_idx_daily = df_global_idx_daily.rename({"day": "date"}, axis=1)
        df_global_idx_daily['date'] = df_global_idx_daily['date'].astype(str)

        Saver.save_to_mysql(df_global_idx_daily,self.sql_table_name)

    def get_global_idx_daily(self, start_date='', end_date=''):
        df_global_idx_daily = self.query_by_condition(condition={"date": (start_date, end_date)})
        return df_global_idx_daily

if __name__=='__main__':
    global_Idx_Daily = Global_Idx_Daily()
    #global_Idx_Daily.save_by_query_date('2020-07-01')

    #df = global_Idx_Daily.query_by_condition({"date":"2020-07-01"})
    df = global_Idx_Daily.get_global_idx_daily(start_date='2020-07-01', end_date='2020-07-06')
    print(df)
