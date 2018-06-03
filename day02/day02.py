# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:35:56 2018

@author: lenovo
"""
import urllib.request as r
city_pinyin=input("请输入城市拼音:")
address='http://api.openweathermap.org/data/2.5/forecast?q=shanghai,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
print(info)

import json
data=json.loads(info)

print("欢迎使用全球天气app")
print("1.查看当前城市天气","2.查看其它城市天气","3.保存当前城市")
menno=input("请输入菜单：")
if menno=="1":
    print("1.查看当前城市未来五天天气")
    print("当前城市为:"+city_pinyin)
    print("#####6月3日#####"+'\n'+str(data["list"][3]['weather'][0]['description'])+'\n'+
          "--Maximum temperature:"+str(data["list"][3]["main"]["temp_max"])+'\n'+
          "--Minimum temperature:"+str(data["list"][3]["main"]["temp_min"]))

    print("#####6月4日#####"+'\n'+str(data["list"][11]['weather'][0]['description'])+'\n'+
          "--Maximum temperature:"+str(data["list"][11]["main"]["temp_max"])+'\n'+
          "--Minimum temperature:"+str(data["list"][11]["main"]["temp_min"]))
    
    print("#####6月5日#####"+'\n'+str(data["list"][19]['weather'][0]['description'])+'\n'+
          "--Maximum temperature:"+str(data["list"][19]["main"]["temp"])+'\n'+
          "--Minimum temperature:"+str(data["list"][19]["main"]["temp_min"]))
    
    print("#####6月6日#####"+'\n'+str(data["list"][27]['weather'][0]['description'])+'\n'+
          "--Maximum temperature:"+str(data["list"][27]["main"]["temp"])+'\n'+
          "--Minimum temperature:"+str(data["list"][27]["main"]["temp_min"]))

    print("#####6月7日#####"+'\n'+str(data["list"][35]['weather'][0]['description'])+'\n'+
          "--Maximum temperature:"+str(data["list"][35]["main"]["temp"])+'\n'+
          "--Minimum temperature:"+str(data["list"][35]["main"]["temp_min"]))
    
if menno=="2":
    print("2.查看其他城市天气")
if menno=="3":
    print("3.保存当前城市")
