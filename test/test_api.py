import tushare as ts
pro = ts.pro_api('c503c99ce9cabcaf1eef092a42a9157a9293386c3e76ef5721ef5c9f')
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,market,list_date')
data.to_excel("../data/stock_basic.xlsx")


