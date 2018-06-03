# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 14:32:45 2018

@author: lenovo
"""
import urllib.request as r
city_pinyin=input("请输入城市拼音:")
address='api.openweathermap.org/data/2.5/weather?q=beijing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
print(info)

import json
data=json.loads(info)


data['main']['temp']
data['main']['temp_max']
data['main']['pressure']
print('最高气温'+str(data['main']['temp_max']))
print('气压'+str(data['main']['pressure']))
print('天气情况'+str(data['weather'][0]['description']))