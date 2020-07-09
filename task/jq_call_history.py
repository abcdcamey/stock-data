from datetime import datetime,timedelta
from request.JoinQuant.All_Securities import All_Securities
from request.JoinQuant.Daily_Securities_Price import Daily_Securities_Price
from request.JoinQuant.Billboard_List import Billboard_List
from request.JoinQuant.Global_Idx_Daily import Global_Idx_Daily
from request.JoinQuant.HK_Hold_Info import HK_Hold_Info
from request.JoinQuant.Money_Flow import Money_Flow
from request.JoinQuant.MTSS import MTSS
from request.JoinQuant.Securities_Fundamentals import Securities_Fundamentals
from request.JoinQuant.Shareholds_Share_Change import Shareholds_Share_Change
if __name__=='__main__':
    date_start = datetime(2017,1,1)
    date_end = datetime(2018, 1, 1)#datetime.now()
    date_list = []
    for i in range(1000):
        date_cur = date_start+timedelta(days=i)
        if date_cur>=date_end:
            break
        date_list.append(str(date_cur.date()))

    all_Securities = All_Securities()
    daily_Securities_Price = Daily_Securities_Price()
    billboard_List = Billboard_List()
    global_Idx_Daily = Global_Idx_Daily()
    hk_Hold_Info = HK_Hold_Info()
    money_Flow = Money_Flow()
    mtss = MTSS()
    securities_Fundamentals = Securities_Fundamentals()
    shareholds_Share_Change = Shareholds_Share_Change()
    for d in date_list:
        print(d)
        all_Securities.save_by_query_date(d,type='stock')
        all_Securities.save_by_query_date(d,type='index')

        #保存日线
        df_all_Securities = all_Securities.query_by_condition(condition={"date":d,"type":"stock"})
        securities_list = list(df_all_Securities['code'])
        daily_Securities_Price.save_by_query_date(securities_list,start_date=d,end_date=d)

        #保存指数
        df_all_Index = all_Securities.query_by_condition(condition={"date": d, "type": "index"})
        index_list = list(df_all_Index['code'])
        daily_Securities_Price.save_by_query_date(index_list,start_date=d,end_date=d)

        billboard_List.save_by_query_date(d)
        global_Idx_Daily.save_by_query_date(d)
        hk_Hold_Info.save_by_query_date(d)
        #
        money_Flow.save_by_query_date(securities_list,start_date=d,end_date=d)
        mtss.save_by_query_date(securities_list,start_date=d,end_date=d)
        securities_Fundamentals.save_by_query_date(securities_list,date=d)
        shareholds_Share_Change.save_by_query_date(securities_list,date=d)

        # money_Flow.save_by_query_date(start_date=d, end_date=d)
        # mtss.save_by_query_date(start_date=d, end_date=d)
        # securities_Fundamentals.save_by_query_date(date=d)
        # shareholds_Share_Change.save_by_query_date(date=d)