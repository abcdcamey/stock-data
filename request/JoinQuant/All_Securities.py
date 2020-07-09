from api.common.JQSDK_Connect import JQSDK_Connect
from api.common.Saver import Saver
from api.common.Query import Query
from request.JoinQuant.Base_Object import Base_Object
from jqdatasdk import *

class All_Securities(Base_Object):
    def __init__(self):
        self.sql_table_name = "jq_all_securities"

    def save_by_query_date(self,date,type='stock'):
        # 获取所有股票
        df_all_securities = get_all_securities(types=[type], date=date)
        df_all_securities = df_all_securities.reset_index(drop=False)
        df_all_securities['date'] = date
        df_all_securities = df_all_securities.rename({"index":"code"},axis=1)
        Saver.save_to_mysql(df_all_securities,self.sql_table_name)

    def query_by_last(self,type='stock'):
        # 获取所有股票
        _df =  Query.query(["*"], self.sql_table_name,tail_condition="order by date desc limit 1")
        last_date = _df.iloc[0].date
        return Query.query(["*"], self.sql_table_name,{"date":last_date})

if __name__=='__main__':
    all_Securities = All_Securities()
    #all_Securities.save_by_query_date('2020-07-02')
    #all_Securities.save_by_query_date('2020-07-01',type='index')

    #df = all_Securities.query_by_condition({"date":"2020-07-01","type":"index"})
    df = all_Securities.query_by_last()

    print(df)
