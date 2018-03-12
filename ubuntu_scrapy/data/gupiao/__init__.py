'''
import json
import gupiao.spiders.read_data as read_data
import gupiao.spiders.write_send_email_data as write_send_email_data
def init():                                                                             #初始化gp_is_sendemail.json，值全部为false
    filename_email = 'E:\docker_hard\ubuntu_scrapy\data\gupiao\gp_is_sendemail.json'
    with open(filename_email) as file_obj:
        dic_email = json.load(file_obj)
    is_send_emial_list = dic_email.fromkeys(read_data.gp_code, False)
    write_send_email_data.write_send_email_data(is_send_emial_list)'''







