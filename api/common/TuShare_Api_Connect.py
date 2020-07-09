#coding=utf-8
import tushare as ts
class TuShare_Api_Connect:

    def __init__(self):
        self.api_connect = ts.pro_api('c503c99ce9cabcaf1eef092a42a9157a9293386c3e76ef5721ef5c9f')

    '''
    获取api连接
    '''
    def get_api_connect(self):
        return self.api_connect




