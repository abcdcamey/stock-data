from api.common.JQSDK_Connect import JQSDK_Connect
from api.common.Saver import Saver
from api.common.Query import Query
from jqdatasdk import *

class Base_Object:
    def __init__(self):
        self.sql_table_name = ""

    def save_by_dataframe(self, df):
        Saver.save_to_mysql(df, self.sql_table_name)

    def query_by_condition(self, condition):
        return Query.query(["*"], self.sql_table_name, condition)