#!/usr/bin/python
# -*- coding: utf-8 -*-
#判断是否发送了email
import read_data
import json
import write_send_email_data


# is_send_emial_list = {}     #设置全局变量，判断是否发送email
# COUNT_sent_email = 0
def _init():
    global is_send_emial_list
    #is_send_emial_list = read_data.dic.fromkeys(read_data.gp_code, False)            #读取json数据中的股票代码，并初始化sendemail为False
    #filename_email = 'E:\docker_hard\ubuntu_scrapy\data\gupiao\gp_is_sendemail.json'                #读取gp_is_sendemail.json里的数据
    filename_email = '/data/gupiao/gp_is_sendemail.json'
    with open(filename_email) as file_obj:
        dic_email = json.load(file_obj)
    is_send_emial_list = dic_email
    for key, value in is_send_emial_list.items():
        print ((str(key)), ' sssvalue : ', str(value).encode('raw_unicode_escape'))
_init()



def change_value(dic):
    dic_email = dic
#    print dic_email
    write_send_email_data.write_send_email_data(dic_email)



