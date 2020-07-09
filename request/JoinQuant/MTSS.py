from api.common.JQSDK_Connect import JQSDK_Connect
from api.common.Saver import Saver
from api.common.Query import Query
from request.JoinQuant.Base_Object import Base_Object
from jqdatasdk import *
from request.JoinQuant.All_Securities import All_Securities

class MTSS(Base_Object):
    def __init__(self):
        self.sql_table_name = "jq_mtss"

    def save_by_query_date(self,securities_list=None,start_date="",end_date=""):

        if securities_list is None:
            all_Securities = All_Securities()
            df = all_Securities.query_by_last()
            securities_list = list(df['code'])
        df_mtss = get_mtss(security_list=securities_list, start_date=start_date, end_date=end_date, fields=None, count=None)
        df_mtss['date'] = df_mtss['date'].astype(str)
        df_mtss = df_mtss.rename({"sec_code":"code"},axis=1)

        Saver.save_to_mysql(df_mtss,self.sql_table_name)

    def get_mtss(self, start_date='', end_date=''):
        df_mtss = self.query_by_condition(condition={"date": (start_date, end_date)})
        return df_mtss


if __name__=='__main__':
    mtss = MTSS()
    #mtss.save_by_query_date(start_date="2020-07-01",end_date="2020-07-01")

    #df = mtss.query_by_condition({"date":"2020-07-02"})
    df = mtss.get_mtss(start_date='2020-07-01', end_date='2020-07-06')

    print(df)
