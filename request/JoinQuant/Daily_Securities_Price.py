from api.common.JQSDK_Connect import JQSDK_Connect
from api.common.Saver import Saver
from jqdatasdk import *
from request.JoinQuant.All_Securities import All_Securities
from request.JoinQuant.Base_Object import Base_Object
import pandas as pd
from api.common.Query import Query

class Daily_Securities_Price(Base_Object):
    def __init__(self):
        self.sql_table_name = "jq_daily_securities_price"

    def save_by_query_date(self,securities_list=None,start_date='',end_date=''):
        if securities_list is None:
            all_Securities = All_Securities()
            df = all_Securities.query_by_last()
            securities_list = list(df['code'])
        fields = ['open', 'close', 'low', 'high', 'volume', 'money', 'factor', 'high_limit','low_limit', 'avg', 'pre_close', 'paused', 'open_interest']
        df_price = get_price(securities_list, start_date=start_date, end_date=end_date, frequency='1d',fields = fields, \
                  skip_paused=False, fq='post', panel=False)
        df_price = df_price.rename({"time":"date"},axis=1)
        df_price['date'] = df_price['date'].astype(str)
        Saver.save_to_mysql(df_price,self.sql_table_name)

    def get_pre_adjust_daily_price(self,start_date='',end_date='',type='stock'):

        all_Securities = All_Securities()
        _df = all_Securities.query_by_condition({"date":end_date,"type":type})
        securities_list = list(_df['code'])

        df_enddate_price = self.query_by_condition(condition={"date":end_date,"code":securities_list})
        df_enddate_price = df_enddate_price.rename({"factor":"last_factor"},axis=1)

        df_all_price = self.query_by_condition(condition={"date": (start_date,end_date),"code":securities_list})

        df_merged = pd.merge(df_all_price,df_enddate_price[['code','last_factor']],how='left',on=['code'])

        df_merged['adjust_close'] = df_merged['close']/df_merged['last_factor']
        df_merged['adjust_open'] = df_merged['open']/df_merged['last_factor']
        df_merged['adjust_high'] = df_merged['high']/df_merged['last_factor']
        df_merged['adjust_low'] = df_merged['low']/df_merged['last_factor']
        df_merged['adjust_high_limit'] = df_merged['high_limit']/df_merged['last_factor']
        df_merged['adjust_low_limit'] = df_merged['low_limit']/df_merged['last_factor']
        df_merged['adjust_avg'] = df_merged['avg']/df_merged['last_factor']
        df_merged['adjust_pre_close'] = df_merged['pre_close']/df_merged['last_factor']

        df_merged['adjust_volume'] = df_merged['volume']*df_merged['last_factor']
        return df_merged



if __name__=='__main__':
    daily_Securities_Price = Daily_Securities_Price()
    #daily_Securities_Price.save_by_query_date(securities_list =["000001.XSHG","000002.XSHG"] ,start_date = '2020-07-02',end_date='2020-07-02')
    #daily_Securities_Price.save_by_query_date(start_date='2020-07-02',end_date='2020-07-02')

    df = daily_Securities_Price.get_pre_adjust_daily_price(start_date='2020-05-01',end_date='2020-07-01')
    print(df)