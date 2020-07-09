from api.common.JQSDK_Connect import JQSDK_Connect
from api.common.Saver import Saver
from api.common.Query import Query
from request.JoinQuant.Base_Object import Base_Object
from jqdatasdk import *
from request.JoinQuant.All_Securities import All_Securities

class Money_Flow(Base_Object):
    def __init__(self):
        self.sql_table_name = "jq_money_flow"

    def save_by_query_date(self,securities_list=None,start_date="",end_date=""):
        if securities_list is None:
            all_Securities = All_Securities()
            df = all_Securities.query_by_last()
            securities_list = list(df['code'])
        df_money_flow = get_money_flow(security_list=securities_list, start_date=start_date, end_date=end_date, fields=None, count=None)
        df_money_flow['date'] = df_money_flow['date'].astype(str)
        df_money_flow = df_money_flow.rename({"sec_code":"code"},axis=1)

        Saver.save_to_mysql(df_money_flow,self.sql_table_name)

    def get_money_flow(self, start_date='', end_date=''):
        df_money_flow = self.query_by_condition(condition={"date": (start_date, end_date)})
        return df_money_flow


if __name__=='__main__':
    money_Flow = Money_Flow()
    #money_Flow.save_by_query_date(start_date="2020-07-01",end_date="2020-07-01")

    #df = money_Flow.query_by_condition({"date":"2020-07-02"})
    df = money_Flow.get_money_flow(start_date='2020-07-01', end_date='2020-07-06')

    print(df)
