import datetime
from datetime import date
from datetime import timedelta

year = timedelta(days=365)

print(datetime.datetime.now().strftime('%Y%m%d'))


class test(object):
    def getYesterday(days):
        today = datetime.date.today()
        oneday = datetime.timedelta(days=days)
        yesterday = today - oneday
        return yesterday.strftime('%Y%m%d')
