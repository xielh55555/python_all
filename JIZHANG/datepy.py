import pandas as pd
import datetime 
# from datetime import timedelta
def datelist(beginDate, endDate):
    date_l=[datetime.date.strftime(x,'%Y-%m-%d') for x in list(pd.date_range(start=beginDate, end=endDate))]
    return date_l