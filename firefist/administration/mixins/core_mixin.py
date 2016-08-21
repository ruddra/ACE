import time
import datetime


class FirefistMixin(object):
    def clock(self):
        return time.time()*1000

    def get_timestamp(self, datetime_obj):
        return datetime_obj.timestamp()

    def get_datetime(self, time_stamp):
        return datetime.datetime.fromtimestamp(time_stamp / 1e3)
