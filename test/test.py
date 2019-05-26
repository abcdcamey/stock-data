from datetime import datetime,timedelta
import numpy as np
#print(str(datetime.now()))
print(np.isnan(np.nan))

cur_date = datetime.now()+timedelta(days=-3099)
print(cur_date.date())

s='000795.SZ'
print(s[0:6]<'000795')