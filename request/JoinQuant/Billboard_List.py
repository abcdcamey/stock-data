from api.common.JQSDK_Connect import JQSDK_Connect
from api.common.Saver import Saver
from api.common.Query import Query
from request.JoinQuant.Base_Object import Base_Object
from jqdatasdk import *

class Billboard_List(Base_Object):
    def __init__(self):
        self.sql_table_name = "jq_billboard_list"

    def save_by_query_date(self,date):
        # 获取所有股票
        df_billboard_list = get_billboard_list(start_date=date,end_date=date)
        df_billboard_list = df_billboard_list.rename({"day":"date"},axis=1)
        df_billboard_list['date'] = df_billboard_list['date'].astype(str)
        Saver.save_to_mysql(df_billboard_list,self.sql_table_name)

    def get_billboard_list(self, start_date='', end_date=''):
        df_billboard_list = self.query_by_condition(condition={"date": (start_date, end_date)})
        return df_billboard_list


if __name__=='__main__':
    billboard_List = Billboard_List()
    #billboard_List.save_by_query_date('2020-07-01')

    #df = billboard_List.query_by_condition({"date":"2020-07-01"})
    df=billboard_List.get_billboard_list(start_date='2020-07-01',end_date='2020-07-05')
    print(df)
