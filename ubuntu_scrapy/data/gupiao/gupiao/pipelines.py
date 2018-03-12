# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class GupiaoPipeline(object):
    def process_item(self, item, spider):
        file_w_json_name = '/data/gupiao/gp_write_data.json'
        with open(file_w_json_name, 'w') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)
        return item


'''     def process_item(self, item, spider):
16         base_dir = os.getcwd()
17         filename = base_dir + '/news.json'
18         # 打开json文件，向里面以dumps的方式吸入数据
19         # 注意需要有一个参数ensure_ascii=False ，不然数据会直接为utf编码的方式存入比如
20         # :“/xe15”
21         with codecs.open(filename, 'a') as f:
22             line = json.dumps(dict(item), ensure_ascii=False) + '\n'
23             f.write(line)
24         return item
file_w_name = 'E:\docker_hard\ubuntu_scrapy\data\gupiao\gp_write_data.json'

def write_json_data(data={}):
    with open(file_w_name, 'w') as file_obj:
        dic = json.load(file_obj)
        obj = json.dump(data, file_obj)
        dic.write(obj)
        print("写入json文件：",  dic)'''