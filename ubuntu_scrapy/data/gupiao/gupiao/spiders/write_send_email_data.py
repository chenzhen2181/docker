# -*- coding: utf-8 -*-


import json

def write_send_email_data(data={}):
    #file_w_name = 'E:\docker_hard\ubuntu_scrapy\data\gupiao\gp_is_sendemail.json'
    file_w_name = '/data/gupiao/gp_is_sendemail.json'
    dic = json.dumps(data)
    with open(file_w_name, 'w') as file_obj:
        '''写入json文件'''
        file_obj.write(dic)


