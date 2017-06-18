# -*- coding:utf-8 -*-

'''
使用fake_useragent库，实现伪装生成headers头部user agent值
'''


from fake_useragent import UserAgent
ua = UserAgent()
print(ua.random)
print(ua.random)
print(ua.random)