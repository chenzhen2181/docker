# -*- coding: utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import json
import read_data
import write_send_email_data
def init():                                             #初始化gp_is_sendemail.json，值全部为false
    #filename_email = 'E:\docker_hard\ubuntu_scrapy\data\gupiao\gp_is_sendemail.json'
    filename_email = '/data/gupiao/gp_is_sendemail.json'
    with open(filename_email) as file_obj:
        dic_email = json.load(file_obj)
    is_send_emial_list = dic_email.fromkeys(read_data.gp_code, False)       #字典fromkeys()值都为false
    write_send_email_data.write_send_email_data(is_send_emial_list)

