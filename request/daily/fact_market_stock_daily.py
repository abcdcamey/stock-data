from api.fact.Fact_Market_Stock_Data import Fact_Market_Stock_Data
from api.common.Saver import Saver
dda = Fact_Market_Stock_Data()


Saver.save_to_mysql(dda.get_fact_market_stock_daily(_trade_date='20190401'),
                    'fact_market_stock_daily')

Saver.save_to_mysql(dda.get_fact_market_stock_weekly(_trade_date='20190419'),
                    'fact_market_stock_weekly')

Saver.save_to_mysql(dda.get_fact_market_stock_monthly(_trade_date='20190329'),
                    'fact_market_stock_monthly')





