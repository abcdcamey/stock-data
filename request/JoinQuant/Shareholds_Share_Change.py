from api.common.JQSDK_Connect import JQSDK_Connect
from api.common.Saver import Saver
from api.common.Query import Query
from request.JoinQuant.Base_Object import Base_Object
from jqdatasdk import *
from request.JoinQuant.All_Securities import All_Securities

class Shareholds_Share_Change(Base_Object):
    def __init__(self):
        self.sql_table_name = "jq_shareholds_share_change"

    def save_by_query_date(self,securities_list=None,date=''):
        if securities_list is None:
            all_Securities = All_Securities()
            df = all_Securities.query_by_last()
            securities_list = list(df['code'])

        q = query(finance.STK_SHAREHOLDERS_SHARE_CHANGE).filter(
            finance.STK_SHAREHOLDERS_SHARE_CHANGE.pub_date ==date,
            finance.STK_SHAREHOLDERS_SHARE_CHANGE.code.in_(securities_list))

        df_shareholds_share_change = finance.run_query(q)
        df_shareholds_share_change['pub_date'] = df_shareholds_share_change['pub_date'].astype(str)
        df_shareholds_share_change['end_date'] = df_shareholds_share_change['end_date'].astype(str)

        Saver.save_to_mysql(df_shareholds_share_change,self.sql_table_name)

    def get_shareholds_share_change(self, start_date='', end_date=''):
        df_shareholds_share_change = self.query_by_condition(condition={"pub_date": (start_date, end_date)})
        return df_shareholds_share_change



if __name__=='__main__':
    shareholds_Share_Change = Shareholds_Share_Change()
    #shareholds_Share_Change.save_by_query_date(date="2020-07-06")

    #df = shareholds_Share_Change.query_by_condition({"pub_date":"2020-07-01"})
    df=shareholds_Share_Change.get_shareholds_share_change(start_date='2020-07-01', end_date='2020-07-06')
    print(df)
