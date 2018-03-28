# -*- coding:utf-8 -*-
import fmovice
# import tushare as ts
# df = ts.realtime_boxoffice()
# print(df)
movies = fmovice.Search_Movice("战狼2")
print(movies)