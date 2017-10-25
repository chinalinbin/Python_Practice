# -*- coding:utf-8 -*-

import tushare as ts

df = ts.realtime_boxoffice()
print(df)