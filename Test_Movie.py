# -*- coding:utf-8 -*-
import fmovice
# import tushare as ts
# df = ts.realtime_boxoffice()
# print(df)
movies = fmovice.Search_Movice("嫌疑人X的献身")
print(movies)