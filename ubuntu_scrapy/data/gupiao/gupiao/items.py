# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GupiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    gp_w_code = scrapy.Field()  # 创建空list，从json中读取股票代码
    gp_w_name = scrapy.Field() # 创建空list，从json中读取股票名称
    gp_w_price = scrapy.Field()
    gp_w_is_sendemail = scrapy.Field()
    gp_w_date = scrapy.Field()

