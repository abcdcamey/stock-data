from datetime import datetime,timedelta
import numpy as np
#print(str(datetime.now()))
print(np.isnan(np.nan))

cur_date = datetime.now()+timedelta(days=-1)
print(cur_date.date())