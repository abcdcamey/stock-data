from api.common.JQSDK_Connect import JQSDK_Connect
from api.common.Saver import Saver
from api.common.Query import Query
from request.JoinQuant.Base_Object import Base_Object
from jqdatasdk import *
from request.JoinQuant.All_Securities import All_Securities

class Securities_Fundamentals(Base_Object):
    def __init__(self):
        self.sql_table_name = "jq_securities_fundamentals"

    def save_by_query_date(self,securities_list=None,date=''):
        if securities_list is None:
            all_Securities = All_Securities()
            df = all_Securities.query_by_last()
            securities_list = list(df['code'])
        q = query(
                valuation.code, valuation.day, valuation.market_cap, valuation.pe_ratio, valuation.pb_ratio,valuation.turnover_ratio,
                valuation.capitalization,valuation.circulating_cap,valuation.circulating_market_cap,valuation.pe_ratio_lyr,valuation.ps_ratio,valuation.pcf_ratio
            ).filter(
                # 这里不能使用 in 操作, 要使用in_()函数
                valuation.code.in_(securities_list)
            )

        df_fundamentals = get_fundamentals(q, date=date, statDate=None)
        df_fundamentals = df_fundamentals.rename({"day":"date"},axis=1)
        df_fundamentals['date'] = df_fundamentals['date'].astype(str)

        Saver.save_to_mysql(df_fundamentals,self.sql_table_name)

    def get_securities_fundamentals(self, start_date='', end_date=''):
        df_securities_fundamentals = self.query_by_condition(condition={"date": (start_date, end_date)})
        return df_securities_fundamentals


if __name__=='__main__':
    securities_Fundamentals = Securities_Fundamentals()
    #securities_Fundamentals.save_by_query_date(date="2020-07-01")

    #df = securities_Fundamentals.query_by_condition({"date":"2020-07-01"})
    df = securities_Fundamentals.get_securities_fundamentals(start_date='2020-07-01', end_date='2020-07-06')

    print(df)
