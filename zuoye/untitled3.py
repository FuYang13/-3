# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 15:14:52 2018
"地址"：
"手机号码"："123456"
"寄信人"："jack"
@author: lenovo
"""
msg={"地址":"北京海定区....",
"手机号码":"123456",
 "寄信人":"jack"}
print(msg["地址",msg["手机号码"],msg["寄信人"]）
          
msg={"姓名":"lfy",
     "身高":"180",
     "性别":"男",
     "年龄":"20"}
print(msg["姓名"],msg["身高"],msg["性别"],msg["年龄"]）          
xzq={'name':'薛之谦',
     'songs':['演员','模特','嗯','李白']，
     '昵称':'xiaoxue',
     ''
     }
songs=xzq['songs']


tianqi={'今天天气':'小雨转多雨',
        '未来五天的温度':['24','28','30','25','28'],
        '未来五天的情况':['小雨','多云','晴','晴转多云','小雨'],
        '今天星期几':['1','2','3','4','5','6','7'] }
w=tianqi['今天星期几']
print('今天是星期'+w[4])
print(max(tianqi['未来五天的温度']))



      