# -*- coding: utf-8 -*-

import json
import sys
import is_send_email
#import chardet
reload(sys)
sys.setdefaultencoding('utf-8')
filename = '/data/gupiao/gp_data.json'
#filename = 'E:\docker_hard\ubuntu_scrapy\data\gupiao\gp_data.json'
# json_str = json.dumps(menu)
with open(filename) as f:
    dic = json.load(f)                                       #json转化成字典
#print len(dic)                                              #判断字典key数量
gp_code = []                                                 #创建空list，从json中读取股票代码
gp_name = []                                                 #创建空list，从json中读取股票名称
gp_value_max = []                                            #创建空list，从json中读取股票最大值
gp_value_min = []                                            #创建空list，从json中读取股票最小值
gp_percent = []                                              #创建空list，从json中读取股票变动的百分率

for key, value   in dic.items():                             #遍历字典
    gp_name.append(str(key))                                 #list添加
    gp_code.append(dic[key.decode('utf-8')]["CODE"])         #由于key是中文，先解码为Unicode，再读取股票代码
    gp_value_max.append(dic[key.decode('utf-8')]["MAX"])         #由于key是中文，先解码为Unicode，再读取股票最大值
    gp_value_min.append(dic[key.decode('utf-8')]["MIN"])         #由于key是中文，先解码为Unicode，再读取股票最小值
    gp_percent.append(dic[key.decode('utf-8')]["PERCENT"])       #由于key是中文，先解码为Unicode，再读取股票变动的百分率


'''print gp_code
print gp_code[0]
print len(dic)
print(type(dic))'''
#for key, value in dic.items():
#    print ((str(key)), ' value : ', str(value).encode('raw_unicode_escape'))



#for key, value in is_send_email.is_send_emial_list.items():
#    print ((str(key)), ' sssvalue : ', str(value).encode('raw_unicode_escape'))


